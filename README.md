# online-surveys
Simple dockerized Python/Django app for online survays

App uses two collections in Mongodb: surveys and answers.
Surveys contains survey definitions. Answers collection contains records with asks to fill in a survey. All answers will be added to such a record togather with information closing the ask (the survay cannot be opened again after it was answered).

Example of a survey definition:
```
{
    "_id" : ObjectId("5f525203b0ee31c08c7f10b9"),
    "questions" : [ 
        {
            "id" : "23489y23894t2987",
            "text" : "the first question"
        }, 
        {
            "id" : "23489y23894t2988",
            "text" : "the second question"
        }
    ],
    "name" : "Tell us about your retro CPUs",
    "image" : "cpu.png",
    "submit" : "SEND US YOUR OPINION"
}
```

Example of a record in answers collection.
```
{
    "_id" : ObjectId("5f5346a0bc92b6b1f6aa0e5c"),
    "srv" : "5f525203b0ee31c08c7f10b9"
}
```

A list of answers will be added later, after the survey is filled in together with field named 'done' that closes the survey for any further edition.
