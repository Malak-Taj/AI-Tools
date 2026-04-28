import streamlit as st
# شتت
st.set_page_config(page_title="AI Tools For Students", layout="wide")

st.title("🎓 AI Tools For Students")

tools_data = {
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
            "image": "https://scispace.com/scispace-logo-square.svg"
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
        "Scite": {
            "description": "Tracks paper citations.",
            "use": "Evaluate paper credibility.",
            "strength": "Citation intelligence.",
            "link": "https://scite.ai",
            "image": "https://cdn.scite.ai/assets/images/logo-blue.svg"
        }
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
            "image": "https://cdn.brandfetch.io/id9mVQlyB1/theme/dark/logo.svg?c=1dxbfHSJFAPEGdCLU4o5B"
        },
        "Gamma": {
            "description": "AI presentation creator.",
            "use": "Generate slides fast.",
            "strength": "Very fast creation.",
            "link": "https://gamma.app",
            "image": "https://cdn.brandfetch.io/idAmHoFYTU/theme/dark/logo.svg?c=1dxbfHSJFAPEGdCLU4o5B"
        }
    },

    "Diagrams & Medical Visualization": {
        "Excalidraw": {
            "description": "Create diagrams visually.",
            "use": "Medical concept maps.",
            "strength": "Simple visual learning.",
            "link": "https://excalidraw.com",
            "image": "https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/excalidraw-ro4ioabgnrs59a1pe3vw.png/excalidraw-lbtjv7j78i9h62q36986vh.png?_a=DATAiZAAZAA0"
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


