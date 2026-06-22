from plot import inverse_score, make_radar_chart


def test_inverse_score_returns_best_score_when_all_values_equal():
    assert inverse_score(1.0, 1.0, 1.0) == 5.0


def test_inverse_score_smaller_value_gets_higher_score():
    best_score = inverse_score(0.001, 0.001, 0.01)
    worst_score = inverse_score(0.01, 0.001, 0.01)

    assert best_score == 5.0
    assert worst_score == 1.0
    assert best_score > worst_score


def test_make_radar_chart_creates_png_file(tmp_path):
    metrics = {
        "linear_time": 0.01,
        "binary_time": 0.001,
        "linear_cmp": 100,
        "binary_cmp": 7,
    }
    output_path = tmp_path / "radar.png"

    make_radar_chart(metrics, output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_make_radar_chart_creates_parent_directory(tmp_path):
    metrics = {
        "linear_time": 0.01,
        "binary_time": 0.001,
        "linear_cmp": 100,
        "binary_cmp": 7,
    }
    output_path = tmp_path / "assets" / "radar.png"

    make_radar_chart(metrics, output_path)

    assert output_path.exists()
    assert output_path.parent.exists()
    assert output_path.stat().st_size > 0
