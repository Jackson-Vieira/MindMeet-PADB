# USE CASES

## Autenticacao

Abstrair fazer 2 usuarios fakes
- psicologo
- paciente

/users

## Agendamentos

- Criar um Agendamento OK
{
    day_hour_id,
    psycologist_id,
    patient_id,
    reason
}

- Excluir um agendamento OK
{
    id
}

- Editar um agendamento (data de inicio, data de fim, situacao, nome) OK
{
    day_hour_id,
    situation,
    nome,
    description
}


- Pegar um agendamento por id OK
/agendamentos/<id>

- Filtrar agendamento por uma data
maior que <y>
menor que <y>

## Requests 
- Criar Solicitacao de agendamento
{
    patient_id,
    psycologist_id,
    day_hour_id,
    reason
} 

## Agenda 
- Criar Agenda (automaticamente ao criar um usuario)
- Criar Agenda Day Hour (Horario disponivel)
{
   start_datetime,
   end_datetime
}