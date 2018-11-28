CREATE TABLE auth_group ( 
	id                   integer NOT NULL  ,
	name                 varchar(80) NOT NULL  ,
	CONSTRAINT pk_auth_group PRIMARY KEY ( id ),
	CONSTRAINT sqlite_autoindex_auth_group_1 UNIQUE ( name ) 
 );

CREATE TABLE auth_user ( 
	id                   integer NOT NULL  ,
	password             varchar(128) NOT NULL  ,
	last_login           datetime   ,
	is_superuser         boolean NOT NULL  ,
	username             varchar(150) NOT NULL  ,
	first_name           varchar(30) NOT NULL  ,
	email                varchar(254) NOT NULL  ,
	is_staff             boolean NOT NULL  ,
	is_active            boolean NOT NULL  ,
	date_joined          datetime NOT NULL  ,
	last_name            varchar(150) NOT NULL  ,
	CONSTRAINT pk_auth_user PRIMARY KEY ( id ),
	CONSTRAINT sqlite_autoindex_auth_user_1 UNIQUE ( username ) 
 );

CREATE TABLE auth_user_groups ( 
	id                   integer NOT NULL  ,
	user_id              integer NOT NULL  ,
	group_id             integer NOT NULL  ,
	CONSTRAINT pk_auth_user_groups PRIMARY KEY ( id ),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE ( user_id, group_id ) ,
	FOREIGN KEY ( group_id ) REFERENCES auth_group( id )  ,
	FOREIGN KEY ( user_id ) REFERENCES auth_user( id )  
 );

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups ( group_id );

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups ( user_id );

CREATE TABLE django_content_type ( 
	id                   integer NOT NULL  ,
	app_label            varchar(100) NOT NULL  ,
	model                varchar(100) NOT NULL  ,
	CONSTRAINT pk_django_content_type PRIMARY KEY ( id ),
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE ( app_label, model ) 
 );

CREATE TABLE django_migrations ( 
	id                   integer NOT NULL  ,
	app                  varchar(255) NOT NULL  ,
	name                 varchar(255) NOT NULL  ,
	applied              datetime NOT NULL  ,
	CONSTRAINT pk_django_migrations PRIMARY KEY ( id )
 );

CREATE TABLE django_session ( 
	session_key          varchar(40) NOT NULL  ,
	session_data         text NOT NULL  ,
	expire_date          datetime NOT NULL  ,
	CONSTRAINT pk_django_session PRIMARY KEY ( session_key )
 );

CREATE INDEX django_session_expire_date_a5c62663 ON django_session ( expire_date );

CREATE TABLE application_follow ( 
	id                   integer NOT NULL  ,
	followed_id          integer NOT NULL  ,
	follower_id          integer NOT NULL  ,
	CONSTRAINT pk_application_follow PRIMARY KEY ( id ),
	FOREIGN KEY ( follower_id, followed_id ) REFERENCES auth_user( id, id )  
 );

CREATE INDEX application_follow_follower_id_3bec0026 ON application_follow ( follower_id );

CREATE INDEX application_follow_followed_id_8d990eb8 ON application_follow ( followed_id );

CREATE TABLE application_profile ( 
	id                   integer NOT NULL  ,
	description          varchar(1000)   ,
	user_id              integer NOT NULL  ,
	image_link           varchar(100)   ,
	CONSTRAINT pk_application_profile PRIMARY KEY ( id ),
	CONSTRAINT sqlite_autoindex_application_profile_1 UNIQUE ( user_id ) ,
	FOREIGN KEY ( user_id ) REFERENCES auth_user( id )  
 );

CREATE TABLE application_quack ( 
	id                   integer NOT NULL  ,
	content              varchar(250) NOT NULL  ,
	created_at           datetime NOT NULL  ,
	quacker_id           integer NOT NULL  ,
	CONSTRAINT pk_application_quack PRIMARY KEY ( id ),
	FOREIGN KEY ( quacker_id ) REFERENCES auth_user( id )  
 );

CREATE INDEX application_quack_quacker_id_470602fd ON application_quack ( quacker_id );

CREATE TABLE auth_permission ( 
	id                   integer NOT NULL  ,
	content_type_id      integer NOT NULL  ,
	codename             varchar(100) NOT NULL  ,
	name                 varchar(255) NOT NULL  ,
	CONSTRAINT pk_auth_permission PRIMARY KEY ( id ),
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE ( content_type_id, codename ) ,
	FOREIGN KEY ( content_type_id ) REFERENCES django_content_type( id )  
 );

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission ( content_type_id );

CREATE TABLE auth_user_user_permissions ( 
	id                   integer NOT NULL  ,
	user_id              integer NOT NULL  ,
	permission_id        integer NOT NULL  ,
	CONSTRAINT pk_auth_user_user_permissions PRIMARY KEY ( id ),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE ( user_id, permission_id ) ,
	FOREIGN KEY ( permission_id ) REFERENCES auth_permission( id )  ,
	FOREIGN KEY ( user_id ) REFERENCES auth_user( id )  
 );

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions ( permission_id );

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions ( user_id );

CREATE TABLE django_admin_log ( 
	id                   integer NOT NULL  ,
	object_id            text   ,
	object_repr          varchar(200) NOT NULL  ,
	action_flag          smallint unsigned NOT NULL  ,
	change_message       text NOT NULL  ,
	content_type_id      integer   ,
	user_id              integer NOT NULL  ,
	action_time          datetime NOT NULL  ,
	CONSTRAINT pk_django_admin_log PRIMARY KEY ( id ),
	FOREIGN KEY ( user_id ) REFERENCES auth_user( id )  ,
	FOREIGN KEY ( content_type_id ) REFERENCES django_content_type( id )  
 );

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log ( user_id );

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log ( content_type_id );

CREATE TABLE application_optionalmention ( 
	id                   integer NOT NULL  ,
	mention_id           integer NOT NULL  ,
	quack_id             integer NOT NULL  ,
	CONSTRAINT pk_application_optionalmention PRIMARY KEY ( id ),
	FOREIGN KEY ( quack_id ) REFERENCES application_quack( id )  ,
	FOREIGN KEY ( mention_id ) REFERENCES auth_user( id )  
 );

CREATE INDEX application_optionalmention_quack_id_38e65ca0 ON application_optionalmention ( quack_id );

CREATE INDEX application_optionalmention_mention_id_74c87e7b ON application_optionalmention ( mention_id );

CREATE TABLE auth_group_permissions ( 
	id                   integer NOT NULL  ,
	group_id             integer NOT NULL  ,
	permission_id        integer NOT NULL  ,
	CONSTRAINT pk_auth_group_permissions PRIMARY KEY ( id ),
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE ( group_id, permission_id ) ,
	FOREIGN KEY ( group_id ) REFERENCES auth_group( id )  ,
	FOREIGN KEY ( permission_id ) REFERENCES auth_permission( id )  
 );

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions ( permission_id );

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions ( group_id );
