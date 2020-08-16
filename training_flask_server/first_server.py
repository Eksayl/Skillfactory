from flask import Flask, render_template, request

app = Flask(__name__)


def insertion_sort(unsorted_list):
    """Функция алгоритма сортировки вставкой. Возвращает отсортированный список"""
    for i in range(1, len(unsorted_list)):
        while i != 0 and (unsorted_list[i - 1]) > unsorted_list[i]:
            unsorted_list[i - 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i - 1]
            i -= 1
    return unsorted_list


@app.route('/')
def go():
    filename = 'data.csv'
    with open(filename, 'w') as file_object:
        file_object.write('name')
        file_object.write(',')
        file_object.write('email')
        file_object.write(',')
        file_object.write('answer')
        file_object.write("\n")
    return render_template('test.html')


@app.route('/answer', methods=['POST'])
def nn():
    name = request.form['name']
    email = request.form['email']
    answer = request.form['message']
    filename = 'data.csv'

    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(answer)
        file_object.write("\n")

    return render_template('test.html')


@app.route('/answer2', methods=['POST'])
def sorting():
    string = list(map(int, request.form['string'].split()))
    string = " ".join(map(str, insertion_sort(string)))
    return render_template('pages/first_app_flask.html', ans=string)


@app.route('/test.html')
def index():
    return render_template('test.html')


@app.route('/pages/first_app_flask.html')
def first_app_flask():
    return render_template('pages/first_app_flask.html')


@app.route('/pages/contacts.html')
def contacts():
    return render_template('pages/contacts.html')


@app.route('/pages/mem.html')
def mem():
    return render_template('pages/mem.html')


if __name__ == "__main__":
    app.run(debug=True)