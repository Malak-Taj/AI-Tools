import streamlit as st

# شتت
st.set_page_config(page_title="AI Tools For Students", layout="wide")

st.title("🎓 AI Tools For Students")

tools_data = {
    "Introduction to Prompt Engineering": {
        "Prompt Engineering Guide": {
            "description": "Course material and introduction to prompt engineering.",
            "use": "Learning the fundamentals of crafting effective AI prompts.",
            "strength": "Direct study resource.",
            "link": "https://drive.google.com/file/d/1kX7r80RPOcbfHznkcW5t81sXHcCS1ufZ/view?usp=sharing",
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg"
        },
        "ChatGPT": {
            "description": "Explains difficult concepts in simple language.",
            "use": "Understanding medical and academic topics.",
            "strength": "Interactive and flexible responses.",
            "link": "https://chat.openai.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg"
        },
    },
    "Understanding Concepts": {
        "ChatGPT": {
            "description": "Explains difficult concepts in simple language.",
            "use": "Understanding medical and academic topics.",
            "strength": "Interactive and flexible responses.",
            "link": "https://chat.openai.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg"
        },
        "Gemini": {
            "description": "Google AI assistant for learning and reasoning.",
            "use": "Deep explanations and advanced topics.",
            "strength": "Google ecosystem integration.",
            "link": "https://gemini.google.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Google-gemini-icon.svg"
        },
        "Claude": {
            "description": "Detailed long-form AI assistant.",
            "use": "Complex concept explanation.",
            "strength": "Clear structured answers.",
            "link": "https://claude.ai",
            "image": "https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/light/claude-color.png"
        }
    },

    "Writing & Academic Writing": {
        "Grammarly": {
            "description": "Grammar and writing assistant.",
            "use": "Improve assignments and reports.",
            "strength": "Professional writing enhancement.",
            "link": "https://www.grammarly.com",
            "image": "https://svgstack.com/media/img/grammarly-logo-pScf603681.webp"
        },
        "QuillBot": {
            "description": "Paraphrasing and rewriting tool.",
            "use": "Rewrite academic text.",
            "strength": "Strong paraphrasing engine.",
            "link": "https://quillbot.com",
            "image": "https://cdn.brandfetch.io/idEDptjcNN/w/400/h/400/theme/dark/icon.jpeg?c=1dxbfHSJFAPEGdCLU4o5B"
        },
        "Notion AI": {
            "description": "Writing and note organization inside Notion.",
            "use": "Writing and organizing study notes.",
            "strength": "Writing + productivity together.",
            "link": "https://www.notion.so/product/ai",
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png"
        }
    },

    "Research & Scientific Papers": {
        "Perplexity": {
            "description": "Search engine with cited answers.",
            "use": "Quick scientific research.",
            "strength": "Reliable references.",
            "link": "https://www.perplexity.ai",
            "image": "https://svgstack.com/media/img/perplexity-logo-6QnZ386077.webp"
        },
        "SciSpace": {
            "description": "Explains research papers.",
            "use": "Understanding academic articles.",
            "strength": "Simplifies scientific papers.",
            "link": "https://www.scispace.com",
            "image": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/596315a2-4138-46db-88ef-e58cb629d1fa.png?w=90&h=90&fit=max&dpr=3&auto=format&q=50"
        },
        "Elicit": {
            "description": "Literature review assistant.",
            "use": "Finding and comparing papers.",
            "strength": "Strong for research.",
            "link": "https://elicit.com",
            "image": "https://cdn.brandfetch.io/idMlO-8ors/w/180/h/180/theme/dark/logo.png"
        },
        "Consensus": {
            "description": "Scientific evidence search.",
            "use": "Evidence-based answers.",
            "strength": "Finds scientific consensus.",
            "link": "https://consensus.app",
            "image": "https://cdn.brandfetch.io/id_kzNkZAX/theme/dark/symbol.svg?c=1dxbfHSJFAPEGdCLU4o5B"
        },

    },

    "Notes & Summarization": {
        "NotebookLM": {
            "description": "Summarizes your uploaded files.",
            "use": "Lecture summaries.",
            "strength": "Works on your documents.",
            "link": "https://notebooklm.google",
            "image": "https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/light/notebooklm.png"
        },
        "Mem.ai": {
            "description": "Smart knowledge organization.",
            "use": "Structured notes.",
            "strength": "Auto-linking notes.",
            "link": "https://mem.ai",
            "image": "https://da6jagld7tjfl.cloudfront.net/d1wpcry0qwvomu5n2hyqzfyrp4jo"
        },
        "Otter.ai": {
            "description": "Converts speech to notes.",
            "use": "Lecture transcription.",
            "strength": "Excellent voice notes.",
            "link": "https://otter.ai",
            "image": "https://otter.ai/favicon.ico"
        }
    },

    "Organization & Productivity": {
        "Flow": {
            "description": "Focus management tool.",
            "use": "Study sessions.",
            "strength": "Maintains concentration.",
            "link": "https://www.flow.app",
            "image": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/83/04/7a/83047a1a-6e18-f7bc-3318-322539404844/AppIcon.lsr/400x400bb.webp"
        },
        "Forest": {
            "description": "Focus timer app.",
            "use": "Avoid distractions.",
            "strength": "Motivating focus.",
            "link": "https://www.forestapp.cc",
            "image": "https://www.forestapp.cc/img/icon.png"
        }
    },

    "Presentations & Visual Learning": {
        "Canva": {
            "description": "Design presentations easily.",
            "use": "Create slides.",
            "strength": "Beautiful templates.",
            "link": "https://www.canva.com",
            "image": "https://public.canva.site/logo/media/dfb96cc174513093cd6ed61489ccb750.svg"
        },
        "Gamma": {
            "description": "AI presentation creator.",
            "use": "Generate slides fast.",
            "strength": "Very fast creation.",
            "link": "https://gamma.app",
            "image": "https://i.pinimg.com/736x/28/6e/d1/286ed1c61132d80b2121db757465d225.jpg"
        }
    },

    "Diagrams & Medical Visualization": {
        "Excalidraw": {
            "description": "Create diagrams visually.",
            "use": "Medical concept maps.",
            "strength": "Simple visual learning.",
            "link": "https://excalidraw.com",
            "image": "https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/excalidraw-ro4ioabgnrs59a1pe3vw.png/excalidraw-lbtjv7j78i9h62q36986vh.png?_a=DATAiZAAZAA0"
        },
        "BioDigital Human": {
            "description": "Interactive 3D human anatomy and medical visualization platform.",
            "use": "Studying anatomy, organs, and diseases in 3D.",
            "strength": "Highly visual learning for medical students.",
            "link": "https://human.biodigital.com/explore",
            "image": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/67/1a/1f/671a1f5a-430f-af18-90ff-3f183175bd53/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/246x0w.webp"
        }
    },

    "Career & Interview Prep": {
        "Final Round AI": {
            "description": "AI interview coach.",
            "use": "Interview preparation.",
            "strength": "Professional training.",
            "link": "https://www.finalroundai.com",
            "image": "https://d12araoe7z5xxk.cloudfront.net/landing-page/images/full-logo.svg"
        }
    }
}

category = st.sidebar.radio("Select Category", list(tools_data.keys()))
st.header(category)

tool_names = list(tools_data[category].keys())
tabs = st.tabs(tool_names)

for tab, tool in zip(tabs, tool_names):
    info = tools_data[category][tool]

    with tab:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader(tool)
            st.info(info["description"])
            st.success(f"Best Use: {info['use']}")
            st.warning(f"Strength: {info['strength']}")
            st.link_button("🔗 Visit Website", info["link"])

        with col2:
            st.image(info["image"], use_container_width=True)
