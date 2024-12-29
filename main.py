from flask import Flask, render_template, request

accounts = [
    {
        "name": "Ahmad Irfansyah",
        "no_rekening": 12345678,
        "pin": 123456,
        "saldo": 5000000000000,
    },
    {
        "name": "Setya Andi Wardana",
        "no_rekening": 87654321,
        "pin": 654321,
        "saldo": 150000,
    },
    {
        "name": "Yoga Angga Pratama",
        "no_rekening": 12344321,
        "pin": 123443,
        "saldo": 300000,
    },
    {
        "name": "Stefan William",
        "no_rekening": 43211234,
        "pin": 432112,
        "saldo": 350000,
    },
    {
        "name": "Ari Irham",
        "no_rekening": 87655678,
        "pin": 876521,
        "saldo": 400000,
    },
]

# Membuat aplikasi Flask
app = Flask(__name__)


# Route untuk menampilkan halaman login dan menerima POST untuk memverifikasi login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Ambil data dari form dan konversi ke integer
        try:
            no_rekening = int(request.form.get("rekening"))
            pin = int(request.form.get("pin"))
        except ValueError:
            error_message = "Nomor rekening dan PIN harus berupa angka"
            return render_template("index.html", error_message=error_message)

        # Periksa apakah rekening dan pin cocok dengan salah satu data
        for account in accounts:
            if account["no_rekening"] == no_rekening and account["pin"] == pin:
                return render_template(
                    "home.html",
                    name=account["name"],
                    no_rekening=account["no_rekening"],
                    saldo=account["saldo"],
                )

        # Jika tidak cocok, kembalikan ke halaman login dengan pesan error
        error_message = "Nomor rekening atau PIN salah"
        return render_template("index.html", error_message=error_message)

    return render_template("index.html")


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/tarik-tunai/")
def tarik_tunai():
    return render_template("tarik_tunai.html")


@app.route("/setor-tunai/")
def setor_tunai():
    return render_template("setor_tunai.html")


if __name__ == "__main__":
    app.run(debug=True)
