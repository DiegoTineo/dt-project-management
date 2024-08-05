import uvicorn
import argparse

from app.utils.jwt import createJWT, validateJWT


def print_banner():
    print(
        f"""
         ____  _                    _____ _                  
        |  _ \(_) ___  __ _  ___   |_   _(_)_ __   ___  ___  
        | | | | |/ _ \/ _` |/ _ \    | | | | '_ \ / _ \/ _ \ 
        | |_| | |  __/ (_| | (_) |   | | | | | | |  __/ (_) |
        |____/|_|\___|\__, |\___/    |_| |_|_| |_|\___|\___/ 
                      |___/                                  
            
        PROJECT MANAGEMENT API
            >>> FastAPI 
            >>> SQLAlchemy 
            >>> MySQL
            >>> JWT
            
        """
    )

if __name__ == "__main__":
    try:
        print_banner()
        uvicorn.run("app.app:app", host="0.0.0.0" , port=8000, reload=True)
    except Exception as e:
        print(f"Error: {e}")
