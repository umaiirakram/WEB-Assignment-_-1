# WEB Assignment # 1 -

### Q1: Flexbox in Detail

- **Flex container** - Parent element with `display: flex` that enables flex layout
- **Flex items** - Direct children of flex container become flex items
- **Main axis** - Primary axis defined by flex-direction (horizontal by default)
- **Cross axis** - Perpendicular to main axis (vertical by default)
- **flex-direction** - Sets main axis direction: row, column, row-reverse, column-reverse
- **justify-content** - Aligns items on main axis: flex-start, center, space-between
- **align-items** - Aligns items on cross axis: stretch, center, flex-end
- **flex-wrap** - Controls wrapping: nowrap, wrap, wrap-reverse
- **gap** - Creates space between flex items (row-gap and column-gap)
- **flex-grow** - Defines ability to grow and take free space
- **flex-shrink** - Defines ability to shrink when space is limited

### Q2: CSS Positioning

- **static** - Default position, follows normal document flow
- **relative** - Positioned relative to its normal position
- **absolute** - Positioned relative to nearest positioned ancestor
- **fixed** - Positioned relative to viewport, stays fixed on scroll
- **sticky** - Switches between relative and fixed based on scroll position

Practical example for each method is provided in respective folders with output screenshot.

### Q3: CSS Selectors

- **Universal selector (*)** - Selects all elements on page
- **Element selector (p)** - Selects by tag name
- **Class selector (.class)** - Selects by class name
- **ID selector (#id)** - Selects by id name
- **Attribute selector ([type="text"])** - Selects by attribute value
- **Descendant selector (div p)** - Selects all nested descendants
- **Child selector (div > p)** - Selects only direct children
- **Adjacent sibling selector (h2 + p)** - Selects immediate next sibling
- **General sibling selector (h2 ~ p)** - Selects all following siblings
- **Pseudo-class (:hover, :nth-child)** - Selects special state of element
- **Pseudo-element (::before, ::after)** - Styles specific part of element
