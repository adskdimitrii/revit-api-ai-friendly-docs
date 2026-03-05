# Path Reinforcement Is Valid Rebar Shape Id Method

Source: https://www.revitapidocs.com/2026/0d570de9-c041-3bf2-dff7-47720ee6ace7.htm

---

| Path Reinforcement Is Valid Rebar Shape Id Method |
| --- |

Identifies whether an element id corresponds to a Rebar Shape element which can be used in Path Reinforcement. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsValidRebarShapeId(
	Document aDoc,
	ElementId elementId
)
```

```
Public Shared Function IsValidRebarShapeId ( 
	aDoc As Document,
	elementId As ElementId
) As Boolean
```

```
public:
static bool IsValidRebarShapeId(
	Document^ aDoc, 
	ElementId^ elementId
)
```

```
static member IsValidRebarShapeId : 
        aDoc : Document * 
        elementId : ElementId -> bool 
```

#### Parameters

aDoc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

elementId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   An element id.

#### Return Value

Boolean 
True if the specified element id corresponds to a Rebar Shape element. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The Rebar Shape has to be two dimensional shape only
 and its neighbouring segments may form only right angles.
 Rebar Shapes that have end treatments or crank ar not allowed. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
