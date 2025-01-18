async def help(update, context):
    help_text = """
📚 *Список доступных команд:*

*/add_user <имя>* — Зарегистрироваться в системе.
Пример: `/add_user Саша`

*/delete_user <user_id>* — Удалить пользователя (только для администратора).
Пример: `/delete_user 123456789`

*/make_admin <user_id>* — Назначить пользователя администратором (только для администратора).
Пример: `/make_admin 123456789`

*/add <сумма> <категория> <тип>* — Добавить транзакцию.
Пример: `/add 1000 Еда расход`

*/list* — Посмотреть список всех транзакций.

*/select_user <имя>* — Поменять текущего пользователя.
Пример: `/select_user Саша`

*/delete <id_транзакции>* — Удалить транзакцию по её ID.
Пример: `/delete 1`

*/edit <id_транзакции> <сумма> <категория> <тип>* — Редактировать транзакцию.
Пример: `/edit 1 1500 Еда расход`

*/stats* — Показать статистику по доходам, расходам и распределение по категориям.

*/set_budget <категория> <лимит>* — Установить бюджет для категории.
Пример: `/set_budget Еда 5000`

*/help* — Показать это сообщение.

🛠 *Примеры использования:*
- Добавить доход: `/add 5000 Зарплата доход`
- Добавить расход: `/add 1000 Еда расход`
- Удалить транзакцию: `/delete 1`
- Редактировать транзакцию: `/edit 1 1500 Еда расход`
- Установить бюджет: `/set_budget Еда 5000`
- Назначить администратора: `/make_admin 123456789`
"""

    await update.message.reply_text(help_text, parse_mode="Markdown")