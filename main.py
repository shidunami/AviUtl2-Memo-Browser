from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>シンプルメモ</title>
  <style>
    body {
      font-family: sans-serif;
      background: #f5f5f5;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    textarea {
      width: 100%;
      height: 300px;
      font-size: 16px;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      resize: vertical;
    }
    button {
      margin-top: 10px;
      padding: 10px 15px;
      font-size: 16px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      background: #4CAF50;
      color: white;
      width: 100%;
    }
    button:hover {
      background: #45a049;
    }
  </style>
</head>
<body>
  <h1>メモ</h1>
  <textarea id="memo" placeholder="ここにメモを書いてください"></textarea><br>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
