# Recebendo os dados brutos
initial_day_not_ready = input().split()
initial_time_not_ready = input().split()
final_day_not_ready = input().split()
final_time_not_ready = input().split()

# Preparando os dados de dia e tempo iniciais
initial_day = int(initial_day_not_ready[1])
initial_hour = int(initial_time_not_ready[0])
initial_minute = int(initial_time_not_ready[2])
initial_second = int(initial_time_not_ready[4])

# Preparando os dados de dia e tempo finais
final_day = int(final_day_not_ready[1])
final_hour = int(final_time_not_ready[0])
final_minute = int(final_time_not_ready[2])
final_second = int(final_time_not_ready[4])


total_seconds = abs(final_second - initial_second)
total_minutes = abs(final_minute - initial_minute)
total_hours = abs(final_hour - initial_hour)
total_days = abs(final_day - initial_day)

if final_hour < initial_hour:
    total_days = total_days - 1
    total_hours = 24 - total_hours

# total_days = 0
# total_hours = 0

# if (initial_hour == final_hour and initial_minute == final_minute and initial_second == final_second) == True:
#     total_days = abs(final_day - initial_day)
#     total_hours = 0
# else:
#     if initial_hour < final_hour:
#         total_hours = abs(final_hour - initial_hour)
#         total_days = abs(final_day - initial_day)
#     else:
#         total_hours = 24 - abs(final_hour - initial_hour)
#         if total_hours == 24:
#             total_hours = 0
#             total_days = abs(final_day - initial_day)
#         else:
#             total_days = abs(final_day - initial_day) - 1


# total_seconds = abs(final_second - initial_second)
# total_minutos = abs(final_minute - initial_minute)


print(f'{total_days} dia(s)')
print(f'{total_hours} hora(s)')
print(f'{total_minutes} minuto(s)')
print(f'{total_seconds} segundo(s)')
