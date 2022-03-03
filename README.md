## Assignement
```shell
git clone https://github.com/UnibsMatt/assignement_test.git
cd assignement_test
```
Be sure to have docker installed. Check with the command

```shell
docker -v
> Docker version 20.10.12, build e91ed57
```

Run the api server by typing
```shell
run_all.cmd / run_all.sh
```
This will create the container and run it on your localhost exposing port 5000.   
You can check with 

```shell
docker ps
> af5432cee287   assign    "/bin/sh -c 'python …"   5 minutes ago   Up 5 minutes   0.0.0.0:5000->5000/tcp   assign
```

## V0
The api work by typing the name inside the url on top of the page like:
```
http://localhost:5000/ciao
```
The results it's based on the information given in the task.  
Can be, if the match is found
```html
It seems that marco is from San Marino. But I'm just guessing!
It seems that marco is from Italy. But I'm just guessing!
It seems that marco is from Liechtenstein. But I'm just guessing!
```
or
```html
Sorry no matching found for mastella
```
or 
```html
Opsss. Seems like you have no internet connection
```

## V1
Run all test for the server 'On going'

## V2
Add react front end to send the name through a nicer interface
