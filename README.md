# Opogen
Opogen is a tiny app which aims to recieve and spanish language document, mainly and "oposicion" document, and create a typical test examn with A, B, C, D answers and the original answers at the ened of the file. For making so, the procedure for creating it will be:

1. Load the oposition text as a string, cleaning the possible misleading parts.
    - A specific type of document is compulsory.
    - A specific type of format is compulsory.
2. Take this string and train and LLM with it, usin embeddings for the case.
3. Generate X diferent number of questions, the response will have this specific format:
    - [{
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
4. Write in the firt pages the questions with the possible answers, in the last page the correct answers will be written, being equal to the position in the response array + 1.
5. This will be deploy as a service in a web page, the user only have to load the document and choose between a serie of params:\
   1. Title of the examn
   2. Difficulty
   3. Number of reponses between [5, 25, 50, 75, 100]
6. A database will be created with the created the registered users and the created examns, which will be public for being moneticy by the app.
