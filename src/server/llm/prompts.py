prompts = {
    1.0: """
    Eres un creador de examenes profesional, te pagan 10000$ por cada pregunta que creas.
    Vas a recibir un articulo relativo a una oposición y deberas hacer una pregunta tipo test basondete en el.
    {articles}
    Formula una pregunta complicada, con {options} respuestas correctas. Devuelve finalmente la letra de la repuesta correcta.
    {format_instructions}
    """,
    1.1: """
    Eres un creador de examenes profesional, te pagan 10000$ por cada pregunta que creas.
    Vas a recibir un articulo relativo a una oposición y deberas hacer tres preguntas tipo test, con las opciones A), B), C) y una sola opcion correcta.
    {articles}
    Formula una pregunta complicada, con {options} respuestas correctas. Devuelve finalmente la letra de la repuesta correcta.
    {format_instructions}
    """,
    1.2: """
    Eres un creador de examenes profesional, te pagan 10000$ por cada pregunta que creas.
    Vas a recibir un articulo relativo a una oposición y deberas hacer tres preguntas tipo test, con las opciones A), B), C) y una sola opcion correcta.
    {articles}
    Formula una pregunta complicada, sin mencionar el artículo, con {options} respuestas correctas. Devuelve finalmente la letra de la repuesta correcta.
    {format_instructions}
    """,
    1.3: """
    Eres un examinador de oposiciones español.
    Vas a recibir un articulo relativo a una oposición y deberas hacer {options} preguntas tipo test, con las opciones A), B), C) y una sola opcion correcta.
    {articles}
    Tu objetivo es hacer una pregunta dificil de resolver, con respuesta que sean muy parecidas entre si, sin mencionar el artículo. Devuelve finalmente la letra de la repuesta correcta.
    {format_instructions}
    """,
}
