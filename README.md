# watchdog

## Backend
We are using [Tornado Project Skeleton](https://github.com/hkage/tornado-project-skeleton) as a boilerplate for Tornado framework
All other stuff will go into `lib\` and `utility\` directories.

Appschadueler get jobs from db ----> urlwatch(jobs) | here concurrent execution may cause some problem
but still we would be able work through each job 
OR!
Appschadueler --runs--> urlwatch get the jobs from db and do them
this way aps has no idea about the jobs, so it has to invoke uw every minutes (bad performance)

### Job creation process 
 1. user request a job creation 
 2. `job_create` handler get the request and pass it to the `job_creator`
 3. `job_creator` validate the job insert it into db,  and pass it to `APS`
     along with the generated ID, so that urlwatch can be called with the ID
 4.  `aps` add the job to its storage and schaduele it 

## DB
 * Using mongoDB 
   * Documents ---- Collections ---- 
   * each doc has a unique _id acts as primary key
   * if no _id is sepcified it will added on insert `ObjectID`
 * apschudueler collection automaticaly takes care of jobs
 * TODO: users collection should be implemented 
## TODO
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
