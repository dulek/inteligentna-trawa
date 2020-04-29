Prerequisites
-------------

Before you install and configure the trawa service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``inteligentna_trawa`` database:

     .. code-block:: none

        CREATE DATABASE inteligentna_trawa;

   * Grant proper access to the ``inteligentna_trawa`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON inteligentna_trawa.* TO 'inteligentna_trawa'@'localhost' \
          IDENTIFIED BY 'INTELIGENTNA_TRAWA_DBPASS';
        GRANT ALL PRIVILEGES ON inteligentna_trawa.* TO 'inteligentna_trawa'@'%' \
          IDENTIFIED BY 'INTELIGENTNA_TRAWA_DBPASS';

     Replace ``INTELIGENTNA_TRAWA_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``inteligentna_trawa`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt inteligentna_trawa

   * Add the ``admin`` role to the ``inteligentna_trawa`` user:

     .. code-block:: console

        $ openstack role add --project service --user inteligentna_trawa admin

   * Create the inteligentna_trawa service entities:

     .. code-block:: console

        $ openstack service create --name inteligentna_trawa --description "trawa" trawa

#. Create the trawa service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        trawa public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        trawa internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        trawa admin http://controller:XXXX/vY/%\(tenant_id\)s
