''' 
document:
1. add task: ToDoList.add_task(id, title, created_date, description, tags)
    parameter: id, title, created_date must be given
2. get all tasks: ToDoList.get_all_tasks()
3. get a task: ToDolist.get_task(id)
    parameter: id
4. remove task: ToDolist.remove_task(id)
    parameter: id
5. filter tasks by date: get_task_by_date(start_date, end_date = None)
    parameter:
        start_date: start_date to search tasks
        end_date: end_date to search tasks, if None, only equal search for start_date
6. 
'''
import pandas as pd
import time
import os
import datetime

class ToDoList:
    def __init__(self):
        self.dataFile = 'todo.data';

    def read_csv(self):
        try:
            df = pd.read_csv(self.dataFile)
            return df
        except Exception as e:
            print(e)

    def add_task(self, id, title, created_date, description=None, tag=None):
        d = {'id':[id], 'title': [title], 'created_date':[created_date], 'description':[description], 'tag':[tag]}
        task = pd.DataFrame(data = d)
        hdr = not os.path.exists(self.dataFile) or os.path.getsize(self.dataFile) == 0
        task.to_csv(self.dataFile, mode='a', index = False, header=hdr)

    def get_all_tasks(self):
        print(self.read_csv())

    def get_task(self, id):
        df = self.read_csv()
        df = df[df['id'] == id]
        if df.empty:
            print("no record: id = " + str(id))
        else:
            print(df)

    def remove_task(self, id):
        df = self.read_csv()
        tdf = df[df['id'] == id]
        if tdf.empty:
            print("no record: id = " + str(id) + ", ignore remove task")
            return
        df.drop(df[df['id'] == id].index, inplace=True)
        df.to_csv(self.dataFile, index=False, header=True)
        print("remove record successfully")

    def get_task_by_date(self, start_date, end_date = None):
        df = self.read_csv()
        df.set_index('created_date')
        if end_date:
            df.set_index('created_date', inplace=True)
            date_range = df.loc[str(start_date) : str(end_date)]
            if date_range.empty:
                print("no record find " + str(start_date) + " " + str(end_date))
            else:
                print(date_range)
        else:
            date_range = df[ start_date == df['created_date']]
            if date_range.empty:
                print("\"no record find " + str(start_date) + "\"")
            else:
                print(date_range)

    def get_task_by_tags(self, tags):
        df = self.read_csv()
        for tag in tags:
            tdf = df[df['tag'] == str(tag)]
            if tdf.empty:
                print("no record: tag = " + str(tag))
            else:
                print(tdf)

if __name__=="__main__":
    todo = ToDoList()
    #for x in range (1, 10):
    #    todo.add_task(x, 'title ' + str(x), datetime.datetime.now(), 'description ' + str(x), tag = 'tag ' + str(x))
    #todo.get_all_tasks()
    #x = 1000
    #todo.add_task(x, 'title ' + str(x), datetime.datetime.now())
    #todo.remove_task(-2) #not exists
    #todo.remove_task(4) #success
    #todo.get_task(1)
    #now = datetime.datetime.now()
    #delta = datetime.timedelta(minutes = 10)
    #todo.get_task_by_date(now - delta, now)
    #todo.get_task_by_date('2023-10-04 17:24:33.326760')
    todo.get_task_by_tags(('tag 1', 'tag 3'))
