# watchdog

## Backend
We are using [Tornado Project Skeleton](https://github.com/hkage/tornado-project-skeleton) as a boilerplate for Tornado framework
All other stuff will go into `lib\` and `utility\` directories.

Appschadueler get jobs from db ----> urlwatch(jobs) | here concurrent execution may cause some problem
but still we would be able work through each job 
OR!
Appschadueler --runs--> urlwatch get the jobs from db and do them
this way aps has no idea about the jobs, so it has to invoke uw every minutes (bad performance)

job structure is as follows:
 `Job {
    ID : jobID
    userID : userID
    url : url
    state : state
    repeat :
    Methods : {
        add(schach),
        remove(),
    }
    
 }`
appschadueler 

### TODO
- [ ] http server
- [ ] foolan
- [ ] bahman
- [ ] schadueler
- [ ] urlwatcher

## FrontEnd 
Using [HTML5 Boilerplate](http://www.initializr.com/) Bootstrap 
- [ ] very basic interface
- [ ] add react
- [ ] 
