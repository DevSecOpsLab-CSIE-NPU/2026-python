import io

from data_cleaning import main


def test_main_reads_until_n_zero_no_trailing_blank_line(monkeypatch, capsys):
    # 整合測試：模擬 Sample I/O，確認讀到 n=0 立即停止（不是讀到 EOF），
    # 且輸出剛好兩行、結尾沒有多餘空行或多餘換行符號。
    stdin_text = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(stdin_text))

    main()

    captured = capsys.readouterr()
    # 用完整字串比對，而不是只比對行內容，
    # 才能抓到「結尾多一個空行」這種容易出包的情況
    assert captured.out == "6 9\n3\n"


def test_main_n_zero_immediately_produces_no_output(monkeypatch, capsys):
    # n=0 是第一組就結束，這組不需要處理，也不應該輸出任何東西（包含空行）
    stdin_text = "0\n"
    monkeypatch.setattr("sys.stdin", io.StringIO(stdin_text))

    main()

    captured = capsys.readouterr()
    assert captured.out == ""
