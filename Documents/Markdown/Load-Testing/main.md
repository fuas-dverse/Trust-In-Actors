# Load testing

For load-testing I'm using apache's JMeter tool which is useful to create multiple requests and simulate multiple users. Furthermore they have graphs and tables that can give a good insight on how the application is doing.  
I want to load test the individual sections of the project to find possible problems with having a large amount of people.  
My first instinct of finding where the most problems will come from is first the KafKa MessageBus as this will have the biggest interaction in the entire project and then the websocket server as this will need to hold connections to an UI for the user.  
In principle this can be optimized to close after a certain amount of time or open when something happens. But I haven't tested if this is needed so thats why this load test will be done.

The tests are done using speculations of the final product which is fairly popular. In the real world this will likely not happen as far as I can see. Because it's currently only asking a question waiting for around a minute max for the answer and other than that overview of the current active bots in the system which you can interact with.

## NextJS

I have made a schedule what I think would be reasonable and is just hypothetical on a size of users.
Let's say this will run in a city with around 100,000 people and 10% will be users for the DVerse platform (which is generously overestimated).  
Below you will find the explanation on how it's distributed I can make it more random but that will take to long to make as I need to specify the rate's of users that will be active and spread over a certain amount of time. So the result is below where I make a "normal" distribution of active users between the morning, midday and evening. From 20:00 in the night to 8:00 in the morning is not counted as it will not be used throughout the night, or early mornings in most cases so I didn't include it.

So in the morning (8:00-12:00) we will have around 20% so this will be 2000 users. This should stay steady for a few hours which then ramps down to 0 to simulate nothing happening.
Midday (12:00-16:00) is estimated to have 15% of the active users which has a similar pattern as above with the peak of 1500 users.
We finish with the evening (16:00-20:00) is estimated for 30% of active users with the top being 3000 users. This uses the same pattern as the others.

You can see the following graph for the distribution of the timescale of active users.  
This is used for the chat, containers and login as these are the pages that will commonly be used.  
![graph of distribution of arriving and leaving users ](img/distributionUsers.png)

The next step is running JMeter because of how the active users is implemented this was run over a 15 hour timeframe.  
In the first picture you can see that it started with 1 person. Then 24 users come and on now you can see that for the 24 people in 3 minutes and 30 seconds that 0,1/s comes inside.  
On the last screen you can see in total 78000 users were on the platform on average 462 and had 7249 errors.  
These errors were caused by accidental stopping the platform with closing of visual studio and by high volume of calls that NextJS closed.
![cmd overview of NextJS simulated user access start](img/StartLoadTestNextJS.png)
![cmd overview of NextJS simulated user access end](img/EndLoadTestNextJS.png)

Now that it was run we can see the statistical of the report. But before we go into this we need to define what some things mean.  
HTTP-request means `/chat`  
HTTP-request-0 means `/login`  
HTTP-request-1 means `/container`  
In this table you can see that `/chat` was the most called with 7800 hits. The others have both 47186 total requests. Although this is the most interesting of this table it sets the scene for the following numbers in the table.  
An interesting column is the Transactions per seconds, You can see that although `/chat` is the biggest it handles also the fastest transactions. While `/login` doesn't have that much network so you could think that it should be faster.
![Stats of the JMeter test report](img/Stats.jpeg)
The picture below is for the total amount of request how many did fail. As there is some error margin that is false it does still seem that almost all request when't through successfully
![The amount of errors in the requests with executing the test report](img/RequestsSum.jpeg)
For the APDEX table, it seems that every page is handled the same and that based on the request not any different threshold is active.
![The Application Performance Index](img/APDEX.jpeg)

Now for some more visually pleasing graphs in the next 3 pictures we will have it over the distribution of the responses. So how many where between the reasonable time frame of less then 500ms, how many with less wanted time of >500ms and <1500ms. Which then ends in very late response and errors.

This first picture shows the overview of response time as most response are before the 500ms threshold I need another picture so you can see the amount of the other bars in this graph. See the pictures below
![Overview of response time in full](img/ResponseTimeOverviewzFull.jpeg)
![Overview of response time with higher then 500ms response time](img/ResponseTimeOverviewAbove500.jpeg)

Now for the entire overview although it's not the most readable graph it's still important to show. As you can see that `/chat` has no problem with keeping it between 0 and 100ms. The same can be said about `/login` although it's more visually intensive as other pages it doesn't have a lot in the background on what it needs to do. An example being connecting to the websocket server.  
The `/container` page does also have most responses between 0 and 100ms but a close second comes 100ms and 200ms but this also has more functionality incorporated into it like mouse scrolling (infinity scroll) and the websocket connection.  
There doesn't seem to be any obvious outliers aside from some `/chat` responses with 26 having between 23300ms and 23400ms duration. This is likely a connectivity issue that later resulted in errors.
![Distribution of the response time](img/ResponseTimeDistribution.jpeg)

There are more graphs that give even better insight of this platform so I recommend to look for yourself as it has tooltips that are useful to know the exact amount and you can even zoom in most of the graphs too see each point better. You can find it in this repository under `load-testing-code/JMeter/Results/Index.html`. [direct link](../../../load-testing-code/JMeter/results/demo_results_temp/index.html)

## Websocket server

Although I wanted to load test this also but I couldn't find any tool that could do this I tried with JMeter but I couldn't get it right as it will give me only 404 responses back. With also the difficulty in sending http request without finding some of the connection details such as the generated user id.

So I did it manually in a certain extend I made a loop that requests events from the server and see if a user will be kicked out because the server couldn't handle it. But this is depended on the performance of your own PC as well as this also needs to keep the connections alive.  
You can see the script under load-testing-code, with the name LoadWebServer.py and flaskLoadTest.py. [direct link flask](../../../load-testing-code/flaskLoadTest.py), [direct link WebServer](../../../load-testing-code/LoadWebServer.py)

As a side note with large amounts of simulated people there sometimes is a bug where it activates twice for the same user. But this happens rarely so I don't see any point to worry about this. The cause is likely with the threads that are created.

The conclusion I can make for this is that currently I can not test it to the full capabilities but with 100 simulated users it seems fine to connect and there doesn't seem to be any undue delays.  
Now with the number of 10000 as this is what I took from the NextJS part there also doesn't seem to be any problems with it.
So, I would say the connection is not a problem and only the code itself will cause undue delays.

## Kafka

For to load test kafka I followed a part of the tutorial of [Abhinav Saxena: Let’s Load test, Kafka!](https://medium.com/selectstarfromweb/lets-load-test-kafka-f90b71758afb) on medium. Next to it I also followed one by [zz TALK](https://www.youtube.com/watch?v=jMS6UC1fkRw&t=1s) on youtube that explains how it can be done in JMeter.

Here below is the one by medium, with the standard configuration and sending 100 messages

````Console
 start.time               : 2024–06–11 15:38:28:094 
 end.time                 : 2016–06–11 15:38:28:449 
 compression              : 0
 message.size             : 100
 batch.size               : 200
 total.data.sent.in.MB    : 0.01
 MB.sec                   : 0.0269
 total.data.sent.in.nMsg  : 100
 nMsg.sec                 : 281.6901
````

The one below is where I changed both the compression codec (so less bytes will be send) and buffer.memory set to 100000 just for the reason of having large memory.

````Console
 start.time               : 2024–06–11 15:39:48:094 
 end.time                 : 2016–06–11 15:39:49:449 
 compression              : 0
 message.size             : 100
 batch.size               : 200
 total.data.sent.in.MB    : 0.01
 MB.sec                   : 0.0269
 total.data.sent.in.nMsg  : 100
 nMsg.sec                 : 281.6901
````

But because I did this it did take  longer to finish so I think that it would be better to have the standard configuration.  
I could do further configuration but that is not the point of this as this should be a simple test to see when you change a few configurations what the result is.  
For instance in the server.properties config I could change:

- num.network.threads
- num.io.threads
- socket.send.buffer.bytes
- socket.receive.buffer.bytes
- log.flush.interval.messages
- log.flush.interval.ms

Which can indeed improve performance but that will take a lot of figuring out what the best values are for these configurations and how they affect each other. Such as that with num.io.threads you change processing of the requests, so depending on how good your pc is how higher you can set this so this depends on how much processing power you have available.  
With the log.x configuration means that with higher amounts you will flush later. But this can mean that unflushed data can be lost, but it can also mean that a lot of data needs to be flushed in one period. But when you set it low then it will flush excessively and this can mean that processing power is taken away for sending and receiving messages.

Now for what I did with JMeter, I made a simple test plan that it sends messages with 1 kB of data to Kafka and see what the stats are for sending it.

In the following image you can see a table where the stats of this test plan.  
![Kafka summary](img/KafkaSummaryReport.png)

The following 2 pictures show an example of the producer and consumer. For these picture I find the load time the most important part because of the idea that we investigate how the throughput is for the Kafka MessageBus.
![Kafka producer](img/KafkaProduceMessage.png)
![Kafka consumer](img/KafkaConsumeMessage.png)

## Conclusion

As a conclusion I find that the Kafka server won't need to be changed as it will be fast enough for the purpose intended. The WebSocket server although not tested to the full capabilities won't cause any issues aside from how fast the code itself (other parts of application) or response will be.  
For the NextJS platform was tested the most thorough but aside from some functionality embedded in the page that could be optimized (most likely) it will be enough for the purpose intended and can handle a huge load of users.

As a side note I thought the applications were weaker but they have shown that they can handle a lot. I can say that with it's currently that the only issue you will face that users don't like is the waiting time between the answers on questions from the bots. As this is part of process that's quite long (around 4 programs it needs to go through).

It starts with the platform which sends an event to the WebSocket server, this then sends to a program that determines which actors can handle this, send it to Kafka. The actor itself needs to process the request and then send it back to Kafka going through the WebSocket server and then to the platform.

If we say that each operation takes around 3 seconds (this is a magic number), then it will be 3(NextJS)+3(WebSocket)+3(Agent+topic finder)+3(Kafka)+3(Actor)+3(Kafka)+3(WebSocket)+3(Platform). This is already 24 seconds. That's quite long already, with AI (in the actor) this will take much longer as it needs to start it, wait for the answer and send it back.

This can extend with more if the available actors needs to be found each request and multiple actors need to be done. So if the former is true then another +3 for once and for the latter +(3*n) where n is the number of actors.
