# Teste completo da LeadScript

# Lista de leads simulados
leads = [
    {"email": "a@empresa.com", segmento: "B2B"},
    {"email": "b@empresa.com", segmento: "B2C"},
    {"email": "c@empresa.com", segmento: "B2B"}
]

# Loop sobre leads
para cada lead em leads entao:

    score = classificar_ia(lead, "Validar se o lead e B2B")

    se score > 80 entao:
        enviar_email(lead["email"], "Aprovado", "template.html")
    senao:
        enviar_discord("https://discord.com/api/webhooks/demo", "Lead reprovado: " + lead["email"])
    fim

fim