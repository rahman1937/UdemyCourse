import subprocess
import platform
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_system_uptime() -> Optional[str]:
    """
    Get system uptime in a secure and reliable manner.
    
    Returns:
        str: System uptime string, or None if unable to retrieve
    
    Raises:
        TimeoutError: If subprocess execution exceeds timeout
    """
    try:
        # Platform-specific uptime command
        if platform.system() == 'Windows':
            cmd = ['wmic', 'os', 'get', 'lasbootuptime']
        else:
            cmd = ['uptime']
        
        # Use timeout and specific exception handling for security
        uptime_output = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5,  # 5-second timeout to prevent hanging
            check=True
        )
        
        if uptime_output.returncode != 0:
            logger.warning(f"Command returned non-zero exit code: {uptime_output.returncode}")
            return None
        
        result = uptime_output.stdout.strip()
        logger.info("Successfully retrieved system uptime")
        return result
        
    except subprocess.TimeoutExpired:
        logger.error("Command execution timed out")
        return None
    except subprocess.CalledProcessError as e:
        logger.error(f"Command execution failed: {e.stderr}")
        return None
    except FileNotFoundError:
        logger.error("uptime command not found on this system")
        return None
    except Exception as e:
        logger.error(f"Unexpected error retrieving uptime: {type(e).__name__}: {e}")
        return None

if __name__ == '__main__':
    uptime = get_system_uptime()
    if uptime:
        print(f"System Uptime: {uptime}")
    else:
        print("Failed to retrieve system uptime")
        exit(1)