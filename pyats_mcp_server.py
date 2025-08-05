from pyats.topology import loader
from pyats.async_ import pcall
from mcp import MCP, tool
import logging
from pydantic import BaseModel
	
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load testbed
testbed = loader.load("testbed.yaml")

# Define input schema for validation
class ShowCommandInput(BaseModel):
    device_name: str
    command: str

# Initialize MCP server
app = MCP()

@app.tool()
async def run_show_command(arguments: ShowCommandInput) -> dict:
   """Execute a show command on a Cisco device."""
   device = testbed.devices[arguments.device_name]
   try:
       await device.connect()
       output = await device.execute(arguments.command)
       logger.info(f"Executed '{arguments.command}' on {arguments.device_name}")
       return {"status": "success", "output": output}
   except Exception as e:
       logger.error(f"Failed to execute command: {e}")
       return {"status": "error", "message": str(e)}
   finally:
       await device.disconnect()
if __name__ == "__main__":
	app.run()
