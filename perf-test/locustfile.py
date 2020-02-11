from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def get_content(self):
        self.client.get("/content?contentKey=test")
        
    @task
    def put_content(self):
        data = { "contentKey": "test", "contentValue": "hello world" }
        self.client.put("/content", data=data)

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
