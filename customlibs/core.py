from functools import partial
import math
import multiprocessing as mp
import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats
import sklearn.cluster


def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def filter(data, min_frac):
    data = data.iloc[math.floor(len(data.index) * min_frac) :]
    data = data.dropna(axis=0, how="all")
    data = data.dropna(axis=1)
    return data


def get_return_df(data, periods):
    return_df = data.diff(periods) / data.shift(periods=periods)
    return_df = return_df.dropna(axis=0, how="all")
    return return_df


def anomaly_filter(return_df, max_dev):
    standard_df = (return_df - return_df.mean()) / return_df.std()
    describe_df = standard_df.describe().transpose()
    standard_describe_df = (describe_df - describe_df.mean()) / describe_df.std()
    standard_describe_df = standard_describe_df.dropna(axis=1)
    bool_series = standard_describe_df.apply(lambda x: np.abs(x) < max_dev).all(axis=1)
    column_list = [index for index in bool_series.index if bool_series[index]]
    return return_df[column_list]


def get_mean_series(return_df):
    return return_df.mean(axis=0)


def get_cov_df(return_df):
    return return_df.cov()


def get_shortlist(cov_df, n_clusters):
    kmeans = sklearn.cluster.KMeans(n_clusters=n_clusters)
    kmeans.fit(cov_df.values)
    shortlist = []
    for i, x in enumerate(kmeans.cluster_centers_):
        distance_series = cov_df.apply(lambda y: sum((y - x) ** 2))
        shortlist.append(distance_series.idxmin())
    return list(set(shortlist))


def get_var_mean(mean_vector, cov_matrix, coefs):
    coefs = [x / sum(coefs) for x in coefs]
    coefs_matrix = [[x * y for x in coefs] for y in coefs]
    mean = np.sum(coefs * mean_vector)
    var = np.sum(np.multiply(coefs_matrix, cov_matrix))
    return var, mean


def get_mean(mean_vector, cov_matrix, coefs):
    coefs = [x / sum(coefs) for x in coefs]
    return np.sum(coefs * mean_vector)


def get_var(mean_vector, cov_matrix, coefs):
    coefs = [x / sum(coefs) for x in coefs]
    coefs_matrix = [[x * y for x in coefs] for y in coefs]
    return np.sum(np.multiply(coefs_matrix, cov_matrix))


def optimize(mean_series, cov_df, target_mean):
    init_coefs = [1 / len(mean_series.values) for i in mean_series.values]
    bounds = scipy.optimize.Bounds(0, 1)
    sum_constraint = scipy.optimize.NonlinearConstraint(sum, 1, 1)
    mean_func = partial(get_mean, mean_series.values, cov_df.values)
    mean_constraint = scipy.optimize.NonlinearConstraint(
        mean_func, target_mean, target_mean
    )
    result = scipy.optimize.minimize(
        partial(get_var, mean_series.values, cov_df.values),
        init_coefs,
        bounds=bounds,
        constraints=[sum_constraint, mean_constraint],
    )
    return result


def plot_optimize(mean_series, cov_df, n_points=100):
    target_list = np.linspace(mean_series.min(), mean_series.max(), n_points)
    portfolio_list = []
    pool = mp.Pool()
    optimize_result_list = pool.map(partial(optimize, mean_series, cov_df), target_list)
    pool.close()
    pool.join()
    for optimize_result in optimize_result_list:
        if optimize_result["success"]:
            coefs = list(optimize_result["x"])
            var_mean = get_var_mean(mean_series.values, cov_df.values, coefs)
            portfolio = [coefs, var_mean[0], var_mean[1]]
            portfolio_list.append(portfolio)
    return pd.DataFrame(portfolio_list, columns="coefs var mean".split())


def eliminate(portfolio_df):
    portfolio_df = portfolio_df.sort_values("mean", ascending=False)
    mean_list = list(portfolio_df["mean"].values)
    var_list = list(portfolio_df["var"].values)
    var = var_list[0] + 1
    remove_list = []
    for i in range(len(mean_list)):
        if var_list[i] < var:
            var = var_list[i]
        else:
            remove_list.append(i)
    remove_list = [x for i, x in enumerate(portfolio_df.index) if i in remove_list]
    return portfolio_df.drop(remove_list).reset_index(drop=True)


def metric_to_mean(mean_fit_series, metric_fit_series, order, metric_target_list):
    poly = np.poly1d(np.polyfit(mean_fit_series, metric_fit_series, order))
    mean_target_list = []
    for metric_target in metric_target_list:
        roots = (poly - [0, 0, 0, metric_target]).r
        roots = [x.real for x in roots if x.imag == 0]
        roots = [
            x for x in roots if mean_fit_series.min() <= x <= mean_fit_series.max()
        ]
        if len(roots) != 0:
            mean_target_list.append(roots[0])
    return pd.Series(mean_target_list)


def target_optimize(mean_series, cov_df, target_list):
    portfolio_list = []
    pool = mp.Pool()
    optimize_result_list = pool.map(partial(optimize, mean_series, cov_df), target_list)
    pool.close()
    pool.join()
    for optimize_result in optimize_result_list:
        if optimize_result["success"]:
            coefs = list(optimize_result["x"])
            var_mean = get_var_mean(mean_series.values, cov_df.values, coefs)
            portfolio = [coefs, var_mean[0], var_mean[1]]
            portfolio_list.append(portfolio)
    return pd.DataFrame(portfolio_list, columns="coefs var mean".split())


def get_at_risk(var, mean, percentile):
    return scipy.stats.norm.ppf(percentile, loc=mean, scale=np.sqrt(var))


def get_at_risk_series(portfolio_df, percentile):
    return portfolio_df[["var", "mean"]].apply(
        lambda x: get_at_risk(x[0], x[1], percentile), axis=1
    )


def get_loss_prob(var, mean, loss_size):
    return scipy.stats.norm.cdf(loss_size, loc=mean, scale=np.sqrt(var))


def get_loss_prob_series(portfolio_df, loss_size):
    return portfolio_df[["var", "mean"]].apply(
        lambda x: get_loss_prob(x[0], x[1], loss_size), axis=1
    )


def coefs_to_dict(coefs, ticker_list, min_frac):
    coefs_dict = dict(zip(ticker_list, coefs))
    new_dict = {}
    for key, value in coefs_dict.items():
        if value >= min_frac:
            new_dict[key] = value
    return {key: value * sum(new_dict.values()) for key, value in new_dict.items()}


def coefs_dict_to_string(coefs_dict):
    new_list = [str(key) + str(value) for key, value in coefs_dict.items()]
    return " ".join(new_list)


def get_coefs_dict(portfolio_df, ticker_list, min_frac):
    return portfolio_df["coefs"].apply(
        lambda x: coefs_to_dict(x, ticker_list, min_frac)
    )


def get_coefs_string(portfolio_df):
    return portfolio_df["coefs_dict"].apply(coefs_dict_to_string)
