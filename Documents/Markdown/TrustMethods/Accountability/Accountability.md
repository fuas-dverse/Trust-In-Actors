# Accountability

1. Interface with actors with who has made it, with status and possibly other things.
   - Bot X – Active – Talked with [ “Job”, “Google-bot”, “Bob” ]

1. Log the question and see what route it has taken.
   - E.g.:
      - Question: I want to learn Spanish
      - KeywordMaker: I, learn, Spanish.
      - MessageBus: topic_language
      - Actor: Resource_finder_9000
      - MessageBus: topic_answer
      - User: Learner_Span1sh

1. Send an email to somebody when the container/actor does something wrong (e.x. network traffic too high)
   - E.g.:
        - Docker-In-Docker: Container_X has requested 100mb of data in the last minute.
        - Email-Sender: BotMaker5 has made Container_X so an email will be sent to limit it or request for
        more network data.
        - Docker-Stopper: Stops Container_X and back-ups the files made or inside of the container. So, the
        program can be checked manually or by AI, why it requests so much from the network in a minute.

## Interface

The Interface with actors with who has made it, with status and possibly other things. Is something that should be available in a certain sense.

The point of this scenario is to have a list of which bots are active on the admin/moderators platform. There could be certain things available for it that could work with the docker containers that are available.

Such actions can include disable all bots of a user, delete the bot, request the contents of the bot, restarting of a bot, change their name (which can also be available for the user) and run a command in the container.

Of course there can also be other functions that could help but for now I see the above as the most important functionality that could be included in the DVerse project. Of course it's also possible to do things to the Network, Image, Volumes and Swarm.

How I currently see is using the following table where the container is available per topic:

|Container   |Action                 | Control    |
|------------|-----------------------|------------|
|Container X |[Del] [Con] [CMD] [LOG]|[>] [P] [S] |
|Container Y |[Del] [Con] [CMD] [LOG]|[>] [P] [S] |
|Container Z |[Del] [Con] [CMD] [LOG]|[>] [P] [S] |

`[Del]` means Delete such that you can delete the container immediately/gently.  
[Con] means Contents, in this you can ask the entire contents of the container. Its recommended to combine this with the pause or stop command.  
[CMD] means Command, you can run a command in the container such as `Cat` and `ls`, which you receive the output from.  
[LOG] means Logs, you will get the logs that the container made it can happen that there is no logs as it writes to a volume, file in their system or database which this command has no access to. (Volumes are possible but not expected), the logs can be seen as when you run a container in Docker Desktop in the Logs tab.

This can also be combined with the next section. So it can request the history of the bot from beginning till the end. Which has restrictions on what can be seen as sensitive information can be asked but is not typically expected there needs to separation of history such as concerns as doxing can be prevented.

## Log the Q

See the following example:

- E.g.:
  - Question: I want to learn Spanish
  - KeywordMaker: I, learn, Spanish.
  - MessageBus: topic_language
  - Actor: Resource_finder_9000
  - MessageBus: topic_answer
  - User: Learner_Span1sh

In this scenario the user asks a question (Question), Then it goes to the filtering to which topic it belongs to (KeywordMaker), then it goes through the MessageBus (MessageBus) which can be picked up by an bot/service/person (Actor). When the Actor is finished it goes back through the MessageBus(MessageBus), then at last is goes back to the user that asked the question (User).

Now in this scenario the point is to have a log or see what route it has taken to get to the answer, where has is been and what is the output of it.

This can be something that the User can ask from the system itself and see what happened to their question using the DVerse platform.

## Network traffic

This should monitor the network traffic and if it goes over the magic number then it should take some action against the container. The proposed action is currently to send an email or similar to the builder of the container.

The first part of this is the bot called Docker in Docker or DID for short. DID is a container that runs docker in the dockerHub/docker interface. WHY you ask because now the program can run on somewhere without it being local. Because most of the actions need a part of admin privileges it's highly desirable to wall of the access to this container. Although this won't be completely secure there are ways on how it can be done.

DID purpose is to monitor the network traffic of all containers so it doesn't override the magic number of 100mb of requested resources for their own in a minute.  
Then when it picks up a container that does override it there should be a mechanism todo something about it. So now we come to the next part.

It should send to the message bus so it can be picked up and that its not explicitly referencing another bot.

With the pickup comes the second part of this proposed scenario. The Email-Sender when it receives a container it will try to find the owner and send an email to them. If there isn't any owner it will delete it (but this is done by another bot)

Docker-Stopper is the last part this container should disable the container, request the filesystem and then manually or by AI it should find where the problem lies that it requests so much network. This can then be given to an admin so they can say that they want to disable the account from making bots.

Moderation is moderation but without it you will have the wild west. With this I mean although the fediverse should be a flat hierarchy there still needs to be somebody (or multiple) that has a step up above the rest of the users.
