# Opogen
Opogen is a tiny app that aims to receive a Spanish-language document, mainly an "oposicion" document, and create a typical test exam with A, B, C, and D answers and the original answers at the end of the file. For making it, the procedure for creating it will be:
## To-Do Functionality 
1. Load the opposition text as a string, cleaning up any possible misleading parts.
    - A specific type of document is compulsory.
    - A specific type of format is compulsory.
    - If the file is large, it should be separated into chunks.
2. **Take this string and train and [LLM](https://openai.com/product)** with it, using embeddings for the case or RAGS.
3. **Generate X different number of questions**, and the response will have this specific format:
```
[{
        Question: "Que dice la ley en el apartado 2",
        Possible_answers: {
            A:,
            B:,
            C:,
            D:
        },
        Correct_answer: "A"
        },{
        Question: "Que dice la ley en el apartado 4",
        Possible_answers: {
            A:,
            B:,
            C:,
            D:
        },
        Correct_answer: "B"
        }
    ]
```

4. **Write in the first page the questions with the possible answers**; on the last page the correct answers will be written, being equal to the position in the response array + 1.
5. **This will be deployed as a service on a web page**; the user only has to load the document and choose between a series of parameters:
   1. Title of the exam
   2. Difficulty
   3. Number of responses between [5, 25, 50, 75, 100]
6. A database will be created with the registered users and the created exams, which will be public and monetized by the app.
