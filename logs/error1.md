(03Rag) bogle@Bogles-MacBook-Pro o3-rag-main % uvicorn app:app --reload
INFO: Will watch for changes in these directories: ['/Users/bogle/Dev/ai_for_devs/o3-rag-main']
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [6596] using WatchFiles
Error loading file data/insurance-info.txt
Process SpawnProcess-1:
Traceback (most recent call last):
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/unstructured.py", line 59, in **init**
import unstructured # noqa:F401
ModuleNotFoundError: No module named 'unstructured'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/Users/bogle/mambaforge/lib/python3.10/multiprocessing/process.py", line 314, in \_bootstrap
self.run()
File "/Users/bogle/mambaforge/lib/python3.10/multiprocessing/process.py", line 108, in run
self.\_target(*self.\_args, **self.\_kwargs)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/\_subprocess.py", line 80, in subprocess_started
target(sockets=sockets)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/server.py", line 66, in run
return asyncio.run(self.serve(sockets=sockets))
File "/Users/bogle/mambaforge/lib/python3.10/asyncio/runners.py", line 44, in run
return loop.run_until_complete(main)
File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/server.py", line 70, in serve
await self.\_serve(sockets)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/server.py", line 77, in \_serve
config.load()
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/config.py", line 435, in load
self.loaded_app = import_from_string(self.app)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import_from_string
module = importlib.import_module(module_str)
File "/Users/bogle/mambaforge/lib/python3.10/importlib/**init**.py", line 126, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
File "<frozen importlib._bootstrap>", line 1050, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 883, in exec_module
File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
File "/Users/bogle/Dev/ai_for_devs/o3-rag-main/app.py", line 2, in <module>
from rag_example import search_bike_station
File "/Users/bogle/Dev/ai_for_devs/o3-rag-main/rag_example.py", line 8, in <module>
documents = loader.load()
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/directory.py", line 117, in load
return list(self.lazy_load())
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/directory.py", line 195, in lazy_load
yield from self.\_lazy_load_file(i, p, pbar)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/directory.py", line 233, in \_lazy_load_file
raise e
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/directory.py", line 221, in \_lazy_load_file
loader = self.loader_cls(str(item), **self.loader_kwargs)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_core/\_api/deprecation.py", line 216, in warn_if_direct_instance
return wrapped(self, *args, **kwargs)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/unstructured.py", line 213, in **init**
super().**init**(mode=mode, **unstructured_kwargs)
File "/Users/bogle/mambaforge/lib/python3.10/site-packages/langchain_community/document_loaders/unstructured.py", line 61, in **init**
raise ImportError(
ImportError: unstructured package not found, please install it with `pip install unstructured`
