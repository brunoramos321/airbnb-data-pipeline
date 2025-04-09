
- Airbnb Data Pipeline Schema
-- Author: Bruno Ramos
-- Source data from multiple cities (used for trend analysis, pricing, reviews)

-- PostgreSQL database dump
--

-- Dumped from database version 15.12
-- Dumped by pg_dump version 15.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: fact_calendar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fact_calendar (
    listing_id bigint,
    date date,
    available boolean,
    price numeric,
    minimum_nights integer,
    city text
);


ALTER TABLE public.fact_calendar OWNER TO postgres;

--
-- Name: fact_reviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fact_reviews (
    review_uid text NOT NULL,
    id bigint,
    listing_id bigint,
    date date,
    city text
);


ALTER TABLE public.fact_reviews OWNER TO postgres;

--
-- Name: listings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.listings (
    id bigint NOT NULL,
    host_id bigint,
    host_name text,
    neighbourhood_cleansed text,
    latitude numeric,
    longitude numeric,
    property_type text,
    room_type text,
    accommodates integer,
    bedrooms numeric,
    beds numeric,
    bathrooms numeric,
    price numeric,
    minimum_nights integer,
    maximum_nights integer,
    availability_365 integer,
    number_of_reviews integer,
    last_review date,
    reviews_per_month numeric,
    review_scores_rating numeric,
    instant_bookable boolean,
    host_is_superhost boolean,
    calculated_host_listings_count integer,
    wifi boolean,
    air_conditioning boolean,
    heating boolean,
    washer boolean,
    dryer boolean,
    tv boolean,
    kitchen boolean,
    elevator boolean,
    free_parking_on_premises boolean,
    free_street_parking boolean,
    crib boolean,
    smoke_alarm boolean,
    carbon_monoxide_alarm boolean,
    pool boolean,
    hot_tub boolean,
    gym boolean,
    pets_allowed boolean,
    city text
);


ALTER TABLE public.listings OWNER TO postgres;

--
-- Name: fact_reviews fact_reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_reviews
    ADD CONSTRAINT fact_reviews_pkey PRIMARY KEY (review_uid);


--
-- Name: listings listings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.listings
    ADD CONSTRAINT listings_pkey PRIMARY KEY (id);


--
-- Name: fact_calendar fact_calendar_listing_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_calendar
    ADD CONSTRAINT fact_calendar_listing_id_fkey FOREIGN KEY (listing_id) REFERENCES public.listings(id) ON DELETE CASCADE;


--
-- Name: fact_reviews fact_reviews_listing_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fact_reviews
    ADD CONSTRAINT fact_reviews_listing_id_fkey FOREIGN KEY (listing_id) REFERENCES public.listings(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--
