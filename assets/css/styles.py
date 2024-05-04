main_style_css = """   
    <style>
        button[title="View fullscreen"] {
            visibility: hidden;
        }
        [data-testid=stSidebar] {
            background-color: #FFFFFF;
        }
        .stButton>button {
        background-color: #0066FF; 
        color: white; /* Text */
        }
        .stButton>button:hover {
            background-color: #8F97AF;
            color: white;
        }
        .stButton>button:active,
        .stButton>button:focus {
            box-shadow: none;
            border-color: transparent;
            border: 0em solid #0066FF; /* here configure as your needs */
            color: white !important;
        }
        .element-container {
            border-radius: 10px; 
            overflow: hidden; 
        }
        iframe {
            border-radius: 10px; 
            display: block; 
        }
    </style>"""

menu_style_css = {
    "container": {"padding": "0!important", "background-color": "#f2f4ff"},
    "icon": {"color": "#2B3447", "font-size": "20px"},
    "nav-link": {
        "font-family": "calibri",
        "font-size": "20px",
        "text-align": "left",
        "margin": "5px",
        "--hover-color": "#f2f4ff",
    },
    "nav-link-selected": {"background-color": "#8F97AF"},
}

submenu_style_css = {
    "container": {"padding": "0!important", "background-color": "#f2f4ff"},
    "icon": {"color": "#2B3447", "font-size": "20px"},
    "nav-link": {
        "font-family": "calibri",
        "font-size": "17px",
        "text-align": "left",
        "margin": "5px",
        "--hover-color": "#f2f4ff",
    },
    "nav-link-selected": {"background-color": "#8F97AF"},
}

home_title_css = """
    <style>
        .titulo-grande {
            font-size: 100px;
            text-align: center;
        }
    </style>
"""

home_subtitle_css = """
        <style>
            .subtitulo {
                font-size: 52px;
                text-align: center; 
            }
        </style>
    """
