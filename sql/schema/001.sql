-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2016-11-20 21:08:56.471

-- tables

-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2018-09-20 08:39:36.065

-- tables
-- Table: apps
CREATE TABLE "apps"
(
    "uuid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "timestamp" timestamp NULL DEFAULT now(),
    "repo" text NOT NULL,
    "master_uuid" uuid NOT NULL,
    "staging_uuid" uuid NOT NULL,
    CONSTRAINT "apps_pk" PRIMARY KEY ("uuid")
);

-- Table: config
CREATE TABLE "config"
(
    "config" hstore NOT NULL
);

-- Table: enviornments
CREATE TABLE "enviornments"
(
    "uuid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "timestamp" timestamp NULL DEFAULT now(),
    CONSTRAINT "enviornments_pk" PRIMARY KEY ("uuid")
);

-- Table: services
CREATE TABLE "services"
(
    "uuid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "timestamp" timestamp NULL DEFAULT now(),
    "image" text NOT NULL,
    "environment" uuid NOT NULL,
    CONSTRAINT "services_pk" PRIMARY KEY ("uuid")
);

-- Table: users
CREATE TABLE "users"
(
    "uuid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "timestamp" timestamp NULL DEFAULT now(),
    "username" text NOT NULL,
    "keys" text NOT NULL,
    CONSTRAINT "users_pk" PRIMARY KEY ("uuid")
);

-- foreign keys
-- Reference: environment (table: services)
ALTER TABLE "services" ADD CONSTRAINT "environment"
    FOREIGN KEY ("environment")
    REFERENCES "enviornments" ("uuid")
NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: master_uuid (table: apps)
ALTER TABLE "apps" ADD CONSTRAINT "master_uuid"
    FOREIGN KEY ("master_uuid")
    REFERENCES "services" ("uuid")
NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: staging_uuid (table: apps)
ALTER TABLE "apps" ADD CONSTRAINT "staging_uuid"
    FOREIGN KEY ("staging_uuid")
    REFERENCES "services" ("uuid")
NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- End of file.
