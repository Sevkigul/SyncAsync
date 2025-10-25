# Python — Sync vs Threading vs Asyncio

This project is designed to demonstrate the differences between synchronous (sync), multithreading (threading), and asynchronous (asyncio) programming in Python.
The goal is to perform the same task (fetching data from multiple URLs) using four different methods and observe the execution time differences.

---

##  Code File
**sync_async_comparison.py**

This file compares 4 different approaches:

| Function | Description | Approx. Time |
|------------|-----------|----------------|
| `get_data_sync()` |Runs sequentially (synchronous), waits for each request one by one. | ~30 seconds |
| `get_data_threading()` | Starts each request in a separate thread. | ~3–4 seconds |
| `get_data_async_but_as_wrapper()` | Appears asynchronous but waits sequentially (behaves like synchronous). | ~30 seconds |
| `get_data_async_concurrently()` | Launches all requests at once using (`asyncio.gather`). | ~3–4 seconds |

-----------------------------------------

## Libraries Used
- `requests` — Synchronous HTTP requests  
- `threading` — Parallel requests  
- `aiohttp` — Asynchronous HTTP requests  
- `asyncio` — Event loop management  

--------------------------------------------------

## Sample Execution Results

```text
Sync: ~34.0 sec
Threading: ~4.0 sec
Async wrapper: ~32.0 sec
Async concurrent: ~3.5 sec
