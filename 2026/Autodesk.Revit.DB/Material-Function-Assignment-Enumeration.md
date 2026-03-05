# Material Function Assignment Enumeration

Source: https://www.revitapidocs.com/2026/1cbeb006-f7a2-f6d2-491f-faa0b9a006fc.htm

---

| Material Function Assignment Enumeration |
| --- |

Used in class CompoundStructure to specify the function of a layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum MaterialFunctionAssignment
```

```
Public Enumeration MaterialFunctionAssignment
```

```
public enum class MaterialFunctionAssignment
```

```
type MaterialFunctionAssignment
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Finish1 | 4 | Default priority \= 4 |
| Finish2 | 5 | Default priority \= 5 (The lowest effective priority) |
| Insulation | 3 | Default priority \= 3 |
| Membrane | 100 | A membrane layer must have thickness 0\. It is not represented graphically. |
| None | 0 | Default priority \= 0 This is deprecated and should not be used. |
| StructuralDeck | 200 | Default priority \= 1\. Indicates layer is a structural deck. |
| Structure | 1 | Default priority \= 1 (The highest effective priority) |
| Substrate | 2 | Default priority \= 2 |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The function is used primarily to determine
 layer priority which affects how layers of distinct elements interact at a join. Typically, layers penetrate
 lower priority layers and merge with layers of the same priority. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
