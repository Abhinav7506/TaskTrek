
from flask import Flask, render_template,url_for,redirect,request,jsonify
import mysql.connector


app = Flask(__name__,template_folder='templates') 
app.config['DB_User']="root"
app.config['DB_Host']="localhost"
app.config['DB_Password']="raas@2006"
app.config['DB_Database']="TaskTrek"

def get_db():
    return mysql.connector.connect(
        user=app.config['DB_User'],
        host=app.config['DB_Host'],
        password=app.config['DB_Password'],
        database=app.config['DB_Database']
    )
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/home2')
def home2():
    return render_template('Home2.html')

@app.route('/login')
def login_html():
    return render_template('login.html')

@app.route('/signup')
def signup_html():
    return render_template('Signup.html')

@app.route('/todo')
def todo():
    return render_template('ToDo.html')
@app.route('/notes')
def notes():
    return render_template('Notes.html')
@app.route('/diary')
def diary_html():
    return render_template('Diary.html')




@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data=request.json
        con=get_db()
        cursor=con.cursor()
        query = "INSERT INTO accounts (email, username, password) VALUES (%s, %s, %s)"
        values=(data['email'],data['username'],data['password'])
        cursor.execute(query,values)
        con.commit()
        return jsonify({'message': 'Registration successful!','redirect':'/login'})
    except Exception as e:
            print('Error:', e)
            return jsonify({'error': 'Database error'})
    


    
@app.route('/api/login',methods=['POST'])
def login():
    try:
        data=request.json
        con=get_db()
        cursor=con.cursor()
        query="select * from accounts where username=%s and password=%s"
        values=(data['username'],data['password'])
        cursor.execute(query,values)
        user=cursor.fetchone()

        if user:
            return jsonify({'message':'login successful!','redirect':'/home2'})
        else:
            return jsonify({'error':'invalid credentials'})
    except Exception as e:
        print('Error:',e)
        return jsonify({'error':'Database error'})
    finally:
        cursor.close()
        con.close()

# @app.route('/api/todo', methods=['POST'])
# def todo_api():
#     try:
#         data = request.json  # ✅ Fetch JSON data

#         tasks = data.get('tasks', [])  # ✅ Extract multiple tasks (list of dicts)

#         if not tasks:
#             return jsonify({'error': 'No tasks received!'}), 400

#         con = get_db()
#         cursor = con.cursor()

#         query = "INSERT INTO todo (task, status) VALUES (%s, %s)"

#         for task_data in tasks:
#             task = task_data.get('task', '').strip()
#             status = 1 if task_data.get('status', False) else 0  # ✅ Convert Boolean to MySQL format

#             if task:  # ✅ Prevent empty tasks from being saved
#                 cursor.execute(query, (task, status))

#         con.commit()

#         return jsonify({'message': 'Tasks added successfully!'})

#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({'error': 'Database error'}), 500

#     finally:
#         cursor.close()
#         con.close()




@app.route('/api/notes',methods=['POST'])
def notes_api():
    try:
        data=request.json
        print("Recieved data:",data)
        if 'note' not in data:
            return jsonify({'error':'Invalid input data!'}),400
        con=get_db()
        cursor=con.cursor()
        query="insert into notes (note) values(%s)"
        values=(data['note'],)
        cursor.execute(query,values)
        con.commit()
        print("Data inserted successfully")
        return jsonify({'message':'Note saved successfully!','redirect':'/notes'})
    except Exception as e:
        print('Error:',str(e))
        return jsonify({'error':'Database error!!'}),500
    finally:    
        cursor.close()
        con.close()


@app.route('/api/diary',methods=['POST'])
def diary():
    try:
        data=request.json
        print("Received data:", data)
        if not data or 'Topic' not in data or 'content' not in data:
            return jsonify({'error': 'Invalid input data!'}), 400
        con=get_db()
        cursor=con.cursor()
        cursor.execute("select count(*) from diary where topic=%s",(data['Topic'],))
        exists=cursor.fetchone()[0]
        if exists:
            query="update diary set content=%s where topic=%s"
            values=(data['content'],data['Topic'])
            cursor.execute(query,values)
        else:
            query="insert into diary (Topic,content) values(%s,%s)" 
            values=(data['Topic'],data['content'])
            cursor.execute(query,values)
        con.commit()
        print("Data inserted successfully")  

        return jsonify({'message':'Diary saved succuessfully!','redirect':'/home2'})
    except Exception as e:
        print('Error:',str(e))
        return jsonify({'error':'Database error!!'}),500
    
    
@app.route('/api/get_diary',methods=['GET'])
def get_diary():
    try:
        con=get_db()
        cursor=con.cursor()
        query="select Topic from diary"
        cursor.execute(query)
        diary=cursor.fetchall()
        return jsonify(diary)
    except Exception as e:
        print('Error:',e)
        return jsonify({'error':'Database error'})          
    finally:
        cursor.close()
        con.close()
   

@app.route('/api/display_diary', methods=['GET'])
def display_diary():
    try:
        topic = request.args.get('Topic') 
        if not topic:
            return jsonify({'error': 'Topic parameter is missing'}), 400

        con = get_db()
        cursor = con.cursor()
        query = "SELECT content FROM diary WHERE Topic = %s"
        cursor.execute(query, (topic,))
        result = cursor.fetchone()

        if result:
            return jsonify({"Topic": topic, "content": result[0]})
        else:
            return jsonify({"error": "Diary not found"}), 404
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Database error'}), 500
    finally:
        cursor.close()
        con.close()
   

if __name__ == '__main__':
    app.run(debug=True)