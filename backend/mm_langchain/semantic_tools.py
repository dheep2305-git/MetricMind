"""
MetricMind Semantic Layer

This module exposes only approved business metrics
to the AI Agent.
"""

from semantic_layer import METRICS


def get_metrics():

    return METRICS


def get_metric(metric_name):

    return METRICS.get(metric_name, None)