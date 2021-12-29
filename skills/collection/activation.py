class ActivationSkills():

    @classmethod
    def enable_assistant(cls, **kwargs):
        """
        Plays activation sound and creates the assistant response according to the day hour.
        """

        

    @classmethod
    def disable_assistant(cls, **kwargs):
        """
        - Clear console
        - Shutdown the assistant service
        """


"""
CONTROL_SKILLS = [
    {
        'func': ActivationSkills.assistant_greeting,
        'tags': 'start, hi, hello, start, wake up',
        'description': 'Enables the assistant (ready to hear command)'
    },

    {
        'func': ActivationSkills.disable_assistant,
        'tags': 'bye, shut down, exit, termination',
        'description': 'Stops the assistant service (disable assistant)'
    }
]

BASIC_SKILLS = [

    {
        'enable': True,
        'func': BrowserSkills.open_website_in_browser,
        'tags': 'open',
        'description': 'Opens a domain in browser'
    },

    {
        'enable': True,
        'func': BrowserSkills.tell_me_today_news,
        'tags': 'news, today news',
        'description': 'Tells the daily news (find on Google newsfeed)'
    },

    {
        'enable': True,
        'func': DatetimeSkills.tell_the_time,
        'tags': 'time, hour',
        'description': 'Tells the current time'
    },

    {
        'enable': True,
        'func': DatetimeSkills.tell_the_date,
        'tags': 'date',
        'description': 'Tells the current date'
    },

    {
        'enable': True,
        'func': BrowserSkills.tell_me_about,
        'tags': 'search',
        'description': 'Tells about something based on Google search'
    },

    {
        'enable': True,
        'func': UtilSkills.speech_interruption,
        'tags': 'stop',
        'description': 'Stop/interrupt assistant speech'
    },

    {
        'enable': True,
        'func': AssistantInfoSkills.assistant_help,
        'tags': 'help',
        'description': 'A list with all the available skills'
    },

    {
        'enable': True,
        'func': WeatherSkills.tell_the_weather,
        'tags': 'weather, temperature, weather prediction',
        'description': 'Tells the weather for a location (default in current location)'
    },

    {
        'enable': True,
        'func': AssistantInfoSkills.assistant_check,
        'tags': 'hey, hi',
        'description': 'User check if assistant works'
    },

    {
        'enable': True,
        'func': LibreofficeSkills.open_libreoffice_calc,
        'tags': 'calc, excel',
        'description': 'Opens excel applcation'
    },

    {
        'enable': True,
        'func': LibreofficeSkills.open_libreoffice_writer,
        'tags': 'writer, word',
        'description': 'Opens writer application'
    },

    {
        'enable': True,
        'func': LibreofficeSkills.open_libreoffice_impress,
        'tags': 'impress',
        'description': 'Opens impress application'
    },

    {
        'enable': True,
        'func': SystemHealthSkills.tell_memory_consumption,
        'tags': 'ram, ram usage, memory, memory consumption',
        'description': 'The assistant current memory consumption, '

    },

    {
        'enable': True,
        'func': BrowserSkills.open_in_youtube,
        'tags': 'play',
        'description': 'Plays music in Youtube'
    },

    {
        'enable': True,
        'func': InternetSkills.run_speedtest,
        'tags': 'speedtest, internet speed, ping',
        'description': 'Checks internet speed'
    },

    {
        'enable': True,
        'func': InternetSkills.internet_availability,
        'tags': 'internet conection',
        'description': 'Checks for internet availability'
    },

    {
        'enable': True,
        'func': WordSkills.spell_a_word,
        'tags': 'spell, spell the word',
        'description': 'Spells a word'
    },

    {
        'enable': True,
        'func': ReminderSkills.create_reminder,
        'tags': 'reminder',
        'description': 'Create a time reminder'
    },

    {
        'enable': True,
        'func': AssistantInfoSkills.tell_the_skills,
        'tags': 'skills, your skills, what are your skills',
        'description': 'Tells all assistant available skills'
    },

    {
        'enable': True,
        'func': LinuxAppSkills.open_note_app,
        'tags': 'note',
        'description': 'Ask to create a note'
    },

    {
        'enable': True,
        'func': LinuxAppSkills.open_new_browser_window,
        'tags': 'firefox, open firefox',
        'description': 'Ask to open new browser window'
    },

    {
        'enable': True,
        'func': LinuxAppSkills.open_new_bash,
        'tags': 'bash',
        'description': 'Ask to open new bash'
    },

    {
        'enable': True,
        'func': LocationSkill.get_current_location,
        'tags': 'my location, current location',
        'description': 'Ask to tell you your current location'
    },

    {
        'enable': True,
        'func': HistorySkills.show_history_log,
        'tags': 'history, history log, user history',
        'description': 'Ask to tell you asked commands'
    },

    {
        'enable': True,
        'func': RememberSkills.remember,
        'tags': 'remember',
        'description': 'Remember question - answer pairs'
    },

    {
        'enable': True,
        'func': RememberSkills.tell_response,
        'tags': '',
        'description': 'Util skill, there is no tags to call it'
    },

    {
        'enable': True,
        'func': RememberSkills.clear_learned_skills,
        'tags': 'clear learned skills, drop learned skills, remove learned skills',
        'description': 'Clear the learned skills'
    },

    {
        'enable': True,
        'func': UtilSkills.clear_console,
        'tags': 'clear, clear console',
        'description': 'Clears bash console'
    },

    {
        'enable': True,
        'func': ReminderSkills.set_alarm,
        'tags': 'alarm, set alarm',
        'description': 'Set daily alarm (the assistant service should be running)'
    },

    {
        'enable': True,
        'func': MathSkills.do_calculations,
        'tags': math_tags,
        'description': 'Do basic math calculations in bash terminal e.g " (5+5) ^ 2"'
    },

    {
        'enable': True,
        'func': ConfigurationSkills.configure_assistant,
        'tags': 'configure, change settings',
        'description': 'Change the assistant setting values'
    },

    {
        'enable': True,
        'func': UtilSkills.increase_master_volume,
        'tags': 'increase volume, volume up, speak louder',
        'description': 'Increases the speakers master volume'
    },

    {
        'enable': True,
        'func': UtilSkills.reduce_master_volume,
        'tags': 'reduce volume, volume down',
        'description': 'Decreases the speakers master volume'
    },

    {
        'enable': True,
        'func': UtilSkills.mute_master_volume,
        'tags': 'mute',
        'description': 'Mutes the speakers master volume'
    },

    {
        'enable': True,
        'func': UtilSkills.max_master_volume,
        'tags': 'volume max',
        'description': 'Set max the speakers master volume'
    },

]
"""
        