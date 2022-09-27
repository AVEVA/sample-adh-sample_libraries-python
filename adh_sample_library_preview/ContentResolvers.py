from abc import ABC, abstractmethod
from adh_sample_library_preview.SDS import SdsResultPage, SdsStream



class ContentResolver(ABC):
    def __init__(self, response, value_class = None, content = None) -> None:
        self.value_class = value_class
        self.response = response
        self.content = content if content else self.response.json()


    def resolve(self):
        if self.value_class is None:
            return self.content
        else:
            return self._resolve()


    @abstractmethod
    def _resolve(content):
        pass

class ValueContent(ContentResolver):
    def __init__(self, response, value_class) -> None:
        super().__init__(response, value_class)

    def _resolve(self):
        return self.value_class.fromJson(self.response.json())
    

class BulkContent(ContentResolver):
    def __init__(self, response, value_class) -> None:
        super().__init__(response, value_class)


    def _resolve(self):
        values = []
        for valueArray in self.response.json():
            valuesInside = []
            for value in valueArray:
                valuesInside.append(self.value_class.fromJson(value))
            values.append(valuesInside)
        return values
   

class PagedContent(ContentResolver):
    def __init__(self, response, value_class) -> None:
        super().__init__(response, value_class, SdsResultPage.fromJson(response.json()))


    def _resolve(self):
        results = SdsResultPage(results=[], continuation_token=self.content.ContinuationToken)
        if self.content.Results:
            for r in self.content.Results:
                results.Results.append(self.value_class.fromJson(r))
            return results


class DataContent(ContentResolver):
    def __init__(self, response, value_class) -> None:
        super().__init__(response, value_class)


    def _resolve(self):
        content = self.response.json()
        results = []
        for c in content:
            results.append(self.value_class.fromJson(c))
        return results


class StreamsContent(ContentResolver):
    def __init__(self, response) -> None:
        super().__init__(response)


    # Override this to avoid checking for value_class
    def resolve(self):
        return self._resolve()


    def _resolve(self):
        results: list[SdsStream] = []
        for item in self.response.json():
            results.append(SdsStream.fromJson(item))
        return results