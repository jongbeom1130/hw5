from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Univ'] = request.form.get('Univ')
      # 학번
      result['Student Number'] = request.form.get('Num')
      # 성별
      # 학과
      result['Major'] = request.form.get('Major')
      # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨.
      result['Programming Languages'] = ', '.join(request.form.getlist('Pl'))
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
