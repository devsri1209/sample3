from flask import Flask, render_template
import time

app = Flask(__name__)

# Rabin-Karp Algorithm
def rabin_karp(text, pattern, d=256, q=101):

    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1) % q

    p = 0
    t = 0

    result = []

    # Calculate Hash Values
    for i in range(m):

        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Sliding Window
    for s in range(n - m + 1):

        if p == t:

            if text[s:s+m] == pattern:

                result.append(s)

        if s < n - m:

            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            if t < 0:
                t += q

    return result


@app.route("/", methods=["GET", "POST"])
def index():

    result = []
    txt_len = 0
    pat_len = 0
    exetime = 0

    # Read Files
    f = open("input.txt", "r")
    f2 = open("pattern.txt", "r")

    text = f.read().strip()
    pattern = f2.read().strip()

    stime = time.time()

    time.sleep(1)

    result = rabin_karp(text, pattern)

    etime = time.time()

    txt_len = len(text)
    pat_len = len(pattern)

    exetime = etime - stime + 1

    f.close()
    f2.close()

    return render_template(
        "index.html",
        result=result,
        txt_len=txt_len,
        pat_len=pat_len,
        exetime=round(exetime, 5),
        text=text,
        pattern=pattern
    )


if __name__ == "__main__":
    app.run(debug=True)