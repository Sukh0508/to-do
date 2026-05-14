import sqlite3
from flask import Flask, render_template,request , redirect, url_for
def get_con():
    conn = sqlite3.connect("Database.db")
    return conn
conn = get_con() 
cursor = conn.cursor()

cursor.execute("""create table if not exists target(
               name text
)""")
conn.commit()
conn.close()
app = Flask(__name__)
@app.route("/", methods= ["GET","POST"])
def add_task():
    conn = get_con()
    cursor = conn.cursor()
    if request.method == "POST":
     if "edit_btn" in request.form:
        
        old_task = request.form["del"]
        Neww_task = request.form["update_task"]



        cursor.execute("update target set name = ? where name =?",(Neww_task, old_task))

        conn.commit()
        conn.close()
        return redirect("/")
        
     elif "delete_btn" in request.form:
        delname = request.form["del"]

        cursor.execute("delete from target where name = ?",(delname,))
        conn.commit()
        conn.close()
        return redirect("/")
    
   
     elif "task" in request.form and request.form["task"].strip() != "":
         add = request.form["task"]
        
         cursor.execute("insert into target (name) values  (?)",(add,))
         
         conn.commit()
         conn.close()
         return redirect("/")
    # return render_template("index.html")
    conn.close()
    return show()


def show():
    conn = get_con()
    cursor = conn.cursor()
    cursor.execute("select * from target")
    data = cursor.fetchall()
    conn.close()
    print(data)
    return render_template("index.html",task=data) 


   

   

if __name__ == "__main__":
    app.run(host="0.0.0.0")

