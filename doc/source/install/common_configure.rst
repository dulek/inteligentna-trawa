2. Edit the ``/etc/inteligentna_trawa/inteligentna_trawa.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://inteligentna_trawa:INTELIGENTNA_TRAWA_DBPASS@controller/inteligentna_trawa
