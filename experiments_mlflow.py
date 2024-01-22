import mlflow

def calculator(a,b,operation="add"):
    if(operation == "add"):
        return a+b 
    if(operation == "sub"):
        return a-b 
    if(operation == "mul"):
        return a*b 
    if(operation == "divide"):
        return a/b 

if __name__ == "__main__":
    a,b,opt=100,200,"add";
    with mlflow.start_run():
        result = calculator(a,b,opt)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("result",result)
        mlflow.log_param("opt",opt)
        print(result)