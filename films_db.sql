PGDMP         9            
    z            films    15.1    15.1     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16416    films    DATABASE     |   CREATE DATABASE films WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Ukrainian_Ukraine.utf8';
    DROP DATABASE films;
                postgres    false            ?            1259    16423    actors    TABLE     ?   CREATE TABLE public.actors (
    full_name character varying DEFAULT 'noname'::character varying NOT NULL,
    birth_year integer,
    salary integer,
    film_id integer
);
    DROP TABLE public.actors;
       public         heap    postgres    false            ?            1259    16429 	   directors    TABLE     ?   CREATE TABLE public.directors (
    full_name character varying DEFAULT 'noname'::character varying NOT NULL,
    birth_year integer,
    salary integer,
    film_id integer
);
    DROP TABLE public.directors;
       public         heap    postgres    false            ?            1259    16417 
   films_name    TABLE     ?   CREATE TABLE public.films_name (
    id integer,
    full_name character varying DEFAULT 'noname'::character varying NOT NULL,
    release_year integer,
    genre_id integer
);
    DROP TABLE public.films_name;
       public         heap    postgres    false            ?            1259    16436    genre    TABLE     X   CREATE TABLE public.genre (
    id integer NOT NULL,
    genre character varying(50)
);
    DROP TABLE public.genre;
       public         heap    postgres    false            ?            1259    16435    genre_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.genre_id_seq;
       public          postgres    false    218                       0    0    genre_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;
          public          postgres    false    217            t           2604    16439    genre id    DEFAULT     d   ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);
 7   ALTER TABLE public.genre ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218                      0    16423    actors 
   TABLE DATA           H   COPY public.actors (full_name, birth_year, salary, film_id) FROM stdin;
    public          postgres    false    215   `                 0    16429 	   directors 
   TABLE DATA           K   COPY public.directors (full_name, birth_year, salary, film_id) FROM stdin;
    public          postgres    false    216   ?                 0    16417 
   films_name 
   TABLE DATA           K   COPY public.films_name (id, full_name, release_year, genre_id) FROM stdin;
    public          postgres    false    214                    0    16436    genre 
   TABLE DATA           *   COPY public.genre (id, genre) FROM stdin;
    public          postgres    false    218   n                  0    0    genre_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.genre_id_seq', 3, true);
          public          postgres    false    217               O   x?J?L?S??)???4??0?42 NC.??<????̼??J??)??)Hʈ?+5//Q?-?8#?$c?d????? ?w         H   x???Qp?LO?4?47?46 N#??̒?"?????L??)T˥2'1O??(?<(aa?i?0?????? ?.         G   x?3???KU(.?/??4204?4?2??OK?LN?,8??9}R?S?R?A
,8??L8C?+?<S /F??? xr0         (   x?3?L??MM??2?L)J??M?2?LK??̩?????? ???     