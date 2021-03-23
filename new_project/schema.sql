-- Table: public.User

DROP TABLE IF EXISTS "User";

CREATE TABLE "User"
(
    id integer NOT NULL,
    username character varying(255)  NOT NULL,
    "firstName" character varying(255),
    "lastName" character varying(255),
    password character varying(255),
    "createdAt" timestamp with time zone NOT NULL,
    "updatedAt" timestamp with time zone NOT NULL,
    CONSTRAINT "User_pkey" PRIMARY KEY (id),
    CONSTRAINT "User_username_key" UNIQUE (username)
)
