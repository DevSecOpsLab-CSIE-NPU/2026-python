import sys

def to_base3(n: int) -> str:
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(reversed(digits))


def iterative_base3_digit_sum_steps(n: int):
    """Return a list of step strings and the final single-digit result.

    Each step string has the form: "N -> base3 -> sum: S".
    """
    steps = []
    current = n
    # handle zero explicitly
    if current == 0:
        steps.append("0 -> 0 -> sum: 0")
        return steps, 0
    while current >= 10:
        b3 = to_base3(current)
        s = sum(int(d) for d in b3)
        steps.append(f"{current} -> {b3} -> sum: {s}")
        current = s
    return steps, current


def run_cli(data: str):
    data = data.strip()
    if not data:
        return
    try:
        n = int(data)
    except ValueError:
        print("請輸入整數")
        return
    steps, result = iterative_base3_digit_sum_steps(n)
    for s in steps:
        print(s)
    print(f"最終結果：{result}")


def run_gui():
    try:
        import tkinter as tk
        from tkinter import messagebox
    except Exception:
        print("無法載入 Tkinter，請使用命令列模式")
        return

    def on_compute(event=None):
        txt_output.delete('1.0', tk.END)
        raw = entry.get().strip()
        if raw == '':
            return
        try:
            n = int(raw)
        except ValueError:
            messagebox.showerror('錯誤', '請輸入整數')
            return 
        steps, result = iterative_base3_digit_sum_steps(n)
        for s in steps:
            txt_output.insert(tk.END, s + '\n')
        txt_output.insert(tk.END, f"最終結果：{result}\n")

    root = tk.Tk()
    root.title('Base-3 迭代加總')

    frm = tk.Frame(root, padx=8, pady=8)
    frm.pack(fill=tk.BOTH, expand=True)

    lbl = tk.Label(frm, text='輸入十進位整數：')
    lbl.grid(row=0, column=0, sticky='w')

    entry = tk.Entry(frm, width=30)
    entry.grid(row=0, column=1, sticky='we')
    entry.bind('<Return>', on_compute)

    btn = tk.Button(frm, text='計算 (Enter)', command=on_compute)
    btn.grid(row=0, column=2, padx=6)

    txt_output = tk.Text(frm, height=10, width=60)
    txt_output.grid(row=1, column=0, columnspan=3, pady=8)

    # make columns expand
    frm.columnconfigure(1, weight=1)

    entry.focus()
    root.mainloop()


def main():
    # If there's piped input, run CLI mode. Otherwise open GUI (pressing F5 in an editor
    # typically runs the script directly and will show the GUI window).
    if not sys.stdin.isatty():
        data = sys.stdin.read()
        run_cli(data)
    else:
        run_gui()


if __name__ == '__main__':
    main()
