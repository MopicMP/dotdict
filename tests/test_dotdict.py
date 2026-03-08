"""Tests for dotdict."""

import pytest
from dotdict import dotdict


class TestDotdict:
    """Test suite for dotdict."""

    def test_basic(self):
        """Test basic usage."""
        result = dotdict("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            dotdict("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = dotdict(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
