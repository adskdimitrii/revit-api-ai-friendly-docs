# Compound Structure Get Deck Profile Id Method

Source: https://www.revitapidocs.com/2026/995814e7-0265-2472-82b7-8b46586e817c.htm

---

| Compound Structure Get Deck Profile Id Method |
| --- |

Retrieves the profile loop used for the specified structural deck. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetDeckProfileId(
	int layerIdx
)
```

```
Public Function GetDeckProfileId ( 
	layerIdx As Integer
) As ElementId
```

```
public:
ElementId^ GetDeckProfileId(
	int layerIdx
)
```

```
member GetDeckProfileId : 
        layerIdx : int -> ElementId 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

[ElementId](Element-Id-Class.md) 
The element id of a FamilySymbol which contains a profile loop used by a structural deck associated to the specified layer,
 or invalidElementId if isStructuralDeck(layerIdx) is false. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
