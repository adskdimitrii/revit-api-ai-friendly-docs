# Compound Structure Set Deck Profile Id Method

Source: https://www.revitapidocs.com/2026/53707358-b988-204a-7038-708bd47ca835.htm

---

| Compound Structure Set Deck Profile Id Method |
| --- |

Sets the profile loop to use for the specified structural deck. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetDeckProfileId(
	int layerIdx,
	ElementId profileId
)
```

```
Public Sub SetDeckProfileId ( 
	layerIdx As Integer,
	profileId As ElementId
)
```

```
public:
void SetDeckProfileId(
	int layerIdx, 
	ElementId^ profileId
)
```

```
member SetDeckProfileId : 
        layerIdx : int * 
        profileId : ElementId -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

profileId [ElementId](Element-Id-Class.md)
:   The element id of a FamilySymbol which contains a profile loop to be used by the specified layer if it is a structural deck.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer is not a structural deck. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
