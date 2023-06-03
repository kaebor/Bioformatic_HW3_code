from flask import Flask
from flask import render_template
from flask import request
import math

app = Flask(__name__)


@app.route("/")
def input(name=None):
    return render_template('input.html', name=name)


@app.route("/submit", methods=['POST'])
def submit():
    print(request.form.get('sequence'))
    seq = request.form["sequence"]

    X_result = []
    X_count = 0
    X_seq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    seq_len = 0
    print(seq.splitlines(True))
    for i in range(len(seq)):
        if seq[i] == '\n' or seq[i] == '\r\n' or seq[i] == '\r':
            break
        else:
            X_result.append(X_seq[:])
            seq_len += 1
    seq_len_temp = 0
    for i in range(len(seq)):
        if seq[i] == '\n' or seq[i] == '\r\n' or seq[i] == '\r':
            X_count += 1
            seq_len_temp = 0
            continue
        elif seq[i] == 'A':
            X_result[seq_len_temp][0] += 1
        elif seq[i] == 'B':
            X_result[seq_len_temp][1] += 1
        elif seq[i] == 'C':
            X_result[seq_len_temp][2] += 1
        elif seq[i] == 'D':
            X_result[seq_len_temp][3] += 1
        elif seq[i] == 'E':
            X_result[seq_len_temp][4] += 1
        elif seq[i] == 'F':
            X_result[seq_len_temp][5] += 1
        elif seq[i] == 'G':
            X_result[seq_len_temp][6] += 1
        elif seq[i] == 'H':
            X_result[seq_len_temp][7] += 1
        elif seq[i] == 'I':
            X_result[seq_len_temp][8] += 1
        elif seq[i] == 'K':
            X_result[seq_len_temp][9] += 1
        elif seq[i] == 'L':
            X_result[seq_len_temp][10] += 1
        elif seq[i] == 'M':
            X_result[seq_len_temp][11] += 1
        elif seq[i] == 'N':
            X_result[seq_len_temp][12] += 1
        elif seq[i] == 'P':
            X_result[seq_len_temp][13] += 1
        elif seq[i] == 'Q':
            X_result[seq_len_temp][14] += 1
        elif seq[i] == 'R':
            X_result[seq_len_temp][15] += 1
        elif seq[i] == 'S':
            X_result[seq_len_temp][16] += 1
        elif seq[i] == 'T':
            X_result[seq_len_temp][17] += 1
        elif seq[i] == 'V':
            X_result[seq_len_temp][18] += 1
        elif seq[i] == 'W':
            X_result[seq_len_temp][19] += 1
        elif seq[i] == 'Y':
            X_result[seq_len_temp][20] += 1
        elif seq[i] == 'Z':
            X_result[seq_len_temp][21] += 1
        seq_len_temp += 1

    X_count = X_count/2 + 1

    for i in range(len(X_result)):
        for j in range(len(X_result[i])):
            X_result[i][j] = X_result[i][j]/X_count
    print(X_result)

    """
    seq_height = []
    for i in range(len(X_result)):
        Hi = 0
        n = 0
        for j in range(len(X_result[i])):
            if X_result[i][j] > 0:
                n += 1
                Hi = Hi - X_result[i][j] * math.log(X_result[i][j], 2)
            if j == len(X_result[i]) - 1:
                temp_B = 19/(math.log(2, 10)*n*2)
                R = math.log(20, 2) - Hi
                seq_height.append(R)
    print(seq_height)

    for i in range(len(X_result)):
        for j in range(len(X_result[i])):
            X_result[i][j] = X_result[i][j] * seq_height[i]
    print(X_result)
    """

    return render_template('submit.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
