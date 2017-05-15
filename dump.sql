--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: category; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE category (
    category_id integer NOT NULL,
    name character varying(35)
);


ALTER TABLE category OWNER TO vagrant;

--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE category_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_category_id_seq OWNER TO vagrant;

--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE category_category_id_seq OWNED BY category.category_id;


--
-- Name: fermentables; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE fermentables (
    name character varying(35) NOT NULL,
    description character varying(450) NOT NULL,
    "srmId" double precision,
    "moistureContent" double precision,
    "diastaticPower" double precision,
    potential double precision,
    protein double precision,
    "maxInBatch" double precision,
    "requiresMashing" character varying(10),
    characteristics character varying(200),
    country character varying(15)
);


ALTER TABLE fermentables OWNER TO vagrant;

--
-- Name: hops; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE hops (
    name character varying(35) NOT NULL,
    description character varying(1400) NOT NULL,
    "alphaMin" double precision,
    "alphaMax" double precision,
    "betaMin" double precision,
    "betaMax" double precision,
    "originCountry" character varying(20)
);


ALTER TABLE hops OWNER TO vagrant;

--
-- Name: styles; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE styles (
    "styleId" integer NOT NULL,
    name character varying(65) NOT NULL,
    description character varying(2950),
    "abvMin" double precision,
    "abvMax" double precision,
    "ibuMin" double precision,
    "ibuMax" double precision,
    "ogMin" double precision,
    "ogMax" double precision,
    "fgMin" double precision,
    "fgMax" double precision,
    "srmMin" double precision,
    "srmMax" double precision,
    category character varying(35)
);


ALTER TABLE styles OWNER TO vagrant;

--
-- Name: styles_styleId_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE "styles_styleId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "styles_styleId_seq" OWNER TO vagrant;

--
-- Name: styles_styleId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE "styles_styleId_seq" OWNED BY styles."styleId";


--
-- Name: yeasts; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE yeasts (
    yeast_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying(800) NOT NULL,
    "yeastType" character varying(15),
    "fermentTempMin" double precision,
    "fermentTempMax" double precision,
    "alcoholToleranceMin" double precision,
    "alcoholToleranceMax" double precision,
    "yeastFormat" character varying(10)
);


ALTER TABLE yeasts OWNER TO vagrant;

--
-- Name: yeasts_yeast_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE yeasts_yeast_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE yeasts_yeast_id_seq OWNER TO vagrant;

--
-- Name: yeasts_yeast_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE yeasts_yeast_id_seq OWNED BY yeasts.yeast_id;


--
-- Name: category_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category ALTER COLUMN category_id SET DEFAULT nextval('category_category_id_seq'::regclass);


--
-- Name: styleId; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY styles ALTER COLUMN "styleId" SET DEFAULT nextval('"styles_styleId_seq"'::regclass);


--
-- Name: yeast_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY yeasts ALTER COLUMN yeast_id SET DEFAULT nextval('yeasts_yeast_id_seq'::regclass);


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY category (category_id, name) FROM stdin;
\.


--
-- Name: category_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('category_category_id_seq', 1, false);


--
-- Data for Name: fermentables; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY fermentables (name, description, "srmId", "moistureContent", "diastaticPower", potential, protein, "maxInBatch", "requiresMashing", characteristics, country) FROM stdin;
\.


--
-- Data for Name: hops; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY hops (name, description, "alphaMin", "alphaMax", "betaMin", "betaMax", "originCountry") FROM stdin;
\.


--
-- Data for Name: styles; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY styles ("styleId", name, description, "abvMin", "abvMax", "ibuMin", "ibuMax", "ogMin", "ogMax", "fgMin", "fgMax", "srmMin", "srmMax", category) FROM stdin;
\.


--
-- Name: styles_styleId_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('"styles_styleId_seq"', 1, false);


--
-- Data for Name: yeasts; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY yeasts (yeast_id, name, description, "yeastType", "fermentTempMin", "fermentTempMax", "alcoholToleranceMin", "alcoholToleranceMax", "yeastFormat") FROM stdin;
\.


--
-- Name: yeasts_yeast_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('yeasts_yeast_id_seq', 1, false);


--
-- Name: category_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_name_key UNIQUE (name);


--
-- Name: category_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (category_id);


--
-- Name: fermentables_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY fermentables
    ADD CONSTRAINT fermentables_pkey PRIMARY KEY (name);


--
-- Name: hops_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY hops
    ADD CONSTRAINT hops_pkey PRIMARY KEY (name);


--
-- Name: styles_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY styles
    ADD CONSTRAINT styles_pkey PRIMARY KEY ("styleId");


--
-- Name: yeasts_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY yeasts
    ADD CONSTRAINT yeasts_pkey PRIMARY KEY (yeast_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

